/**
 * Project Metrics MCP Server
 *
 * Analyzes code metrics for a project directory.
 * Demonstrates TypeScript MCP patterns from Chapter 18.
 *
 * Tools:
 * - count_lines: Count lines of code by file type
 * - find_todos: Find TODO/FIXME comments
 * - complexity_report: Estimate complexity metrics
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import * as fs from "fs";
import * as path from "path";

const PROJECT_PATH = process.env.PROJECT_PATH || ".";

// File extensions to analyze
const CODE_EXTENSIONS: Record<string, string> = {
  ".ts": "TypeScript",
  ".tsx": "TypeScript/React",
  ".js": "JavaScript",
  ".jsx": "JavaScript/React",
  ".py": "Python",
  ".go": "Go",
  ".rs": "Rust",
  ".java": "Java",
  ".rb": "Ruby",
  ".cpp": "C++",
  ".c": "C",
};

interface FileStats {
  path: string;
  lines: number;
  language: string;
}

interface TodoItem {
  file: string;
  line: number;
  type: string;
  text: string;
}

/**
 * Recursively find all code files in a directory
 */
function findCodeFiles(dir: string, files: string[] = []): string[] {
  try {
    const entries = fs.readdirSync(dir, { withFileTypes: true });

    for (const entry of entries) {
      const fullPath = path.join(dir, entry.name);

      // Skip common non-code directories
      if (entry.isDirectory()) {
        if (!["node_modules", ".git", "dist", "build", "__pycache__", "venv"].includes(entry.name)) {
          findCodeFiles(fullPath, files);
        }
      } else if (entry.isFile()) {
        const ext = path.extname(entry.name);
        if (ext in CODE_EXTENSIONS) {
          files.push(fullPath);
        }
      }
    }
  } catch {
    // Skip directories we can't read
  }

  return files;
}

/**
 * Count lines in a file
 */
function countLines(filePath: string): number {
  try {
    const content = fs.readFileSync(filePath, "utf-8");
    return content.split("\n").length;
  } catch {
    return 0;
  }
}

/**
 * Find TODO/FIXME comments in a file
 */
function findTodosInFile(filePath: string): TodoItem[] {
  const todos: TodoItem[] = [];
  const todoPattern = /\b(TODO|FIXME|HACK|XXX)\b[:\s]*(.*)/gi;

  try {
    const content = fs.readFileSync(filePath, "utf-8");
    const lines = content.split("\n");

    lines.forEach((line, index) => {
      let match;
      while ((match = todoPattern.exec(line)) !== null) {
        todos.push({
          file: path.relative(PROJECT_PATH, filePath),
          line: index + 1,
          type: match[1].toUpperCase(),
          text: match[2].trim() || "(no description)",
        });
      }
    });
  } catch {
    // Skip files we can't read
  }

  return todos;
}

/**
 * Estimate complexity based on control flow keywords
 */
function estimateComplexity(filePath: string): number {
  const complexityKeywords = [
    /\bif\b/g,
    /\belse\b/g,
    /\bfor\b/g,
    /\bwhile\b/g,
    /\bswitch\b/g,
    /\bcatch\b/g,
    /\?\s*.*\s*:/g,  // Ternary
    /&&/g,
    /\|\|/g,
  ];

  try {
    const content = fs.readFileSync(filePath, "utf-8");
    let complexity = 1; // Base complexity

    for (const pattern of complexityKeywords) {
      const matches = content.match(pattern);
      if (matches) {
        complexity += matches.length;
      }
    }

    return complexity;
  } catch {
    return 0;
  }
}

// Create server
const server = new Server(
  { name: "project-metrics", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

// List available tools
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "count_lines",
      description: "Count lines of code in the project, grouped by language",
      inputSchema: {
        type: "object",
        properties: {
          path: {
            type: "string",
            description: "Subdirectory to analyze (optional, defaults to project root)",
          },
        },
      },
    },
    {
      name: "find_todos",
      description: "Find all TODO, FIXME, HACK, and XXX comments in the codebase",
      inputSchema: {
        type: "object",
        properties: {
          type: {
            type: "string",
            description: "Filter by type: TODO, FIXME, HACK, or XXX (optional)",
          },
        },
      },
    },
    {
      name: "complexity_report",
      description: "Generate a complexity report for the codebase. Lists files by estimated cyclomatic complexity.",
      inputSchema: {
        type: "object",
        properties: {
          threshold: {
            type: "number",
            description: "Only show files with complexity above this threshold (default: 10)",
          },
        },
      },
    },
  ],
}));

// Handle tool calls
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  switch (name) {
    case "count_lines": {
      const targetPath = path.resolve(PROJECT_PATH, (args?.path as string) || "");
      const files = findCodeFiles(targetPath);

      const statsByLanguage: Record<string, { files: number; lines: number }> = {};

      for (const file of files) {
        const ext = path.extname(file);
        const language = CODE_EXTENSIONS[ext] || "Other";
        const lines = countLines(file);

        if (!statsByLanguage[language]) {
          statsByLanguage[language] = { files: 0, lines: 0 };
        }
        statsByLanguage[language].files++;
        statsByLanguage[language].lines += lines;
      }

      let report = "## Lines of Code Report\n\n";
      report += "| Language | Files | Lines |\n";
      report += "|----------|-------|-------|\n";

      let totalFiles = 0;
      let totalLines = 0;

      for (const [lang, stats] of Object.entries(statsByLanguage).sort((a, b) => b[1].lines - a[1].lines)) {
        report += `| ${lang} | ${stats.files} | ${stats.lines.toLocaleString()} |\n`;
        totalFiles += stats.files;
        totalLines += stats.lines;
      }

      report += `| **Total** | **${totalFiles}** | **${totalLines.toLocaleString()}** |\n`;

      return { content: [{ type: "text", text: report }] };
    }

    case "find_todos": {
      const files = findCodeFiles(PROJECT_PATH);
      let allTodos: TodoItem[] = [];

      for (const file of files) {
        allTodos = allTodos.concat(findTodosInFile(file));
      }

      // Filter by type if specified
      const filterType = args?.type as string | undefined;
      if (filterType) {
        allTodos = allTodos.filter((t) => t.type === filterType.toUpperCase());
      }

      if (allTodos.length === 0) {
        return { content: [{ type: "text", text: "No TODOs found." }] };
      }

      let report = `## TODO Report (${allTodos.length} items)\n\n`;

      // Group by type
      const byType: Record<string, TodoItem[]> = {};
      for (const todo of allTodos) {
        if (!byType[todo.type]) byType[todo.type] = [];
        byType[todo.type].push(todo);
      }

      for (const [type, todos] of Object.entries(byType)) {
        report += `### ${type} (${todos.length})\n\n`;
        for (const todo of todos.slice(0, 20)) {  // Limit output
          report += `- **${todo.file}:${todo.line}**: ${todo.text}\n`;
        }
        if (todos.length > 20) {
          report += `- *(${todos.length - 20} more...)*\n`;
        }
        report += "\n";
      }

      return { content: [{ type: "text", text: report }] };
    }

    case "complexity_report": {
      const threshold = (args?.threshold as number) || 10;
      const files = findCodeFiles(PROJECT_PATH);

      const complexities: Array<{ file: string; complexity: number }> = [];

      for (const file of files) {
        const complexity = estimateComplexity(file);
        if (complexity >= threshold) {
          complexities.push({
            file: path.relative(PROJECT_PATH, file),
            complexity,
          });
        }
      }

      complexities.sort((a, b) => b.complexity - a.complexity);

      if (complexities.length === 0) {
        return {
          content: [{
            type: "text",
            text: `No files found with complexity >= ${threshold}`,
          }],
        };
      }

      let report = `## Complexity Report\n\n`;
      report += `Files with estimated complexity >= ${threshold}:\n\n`;
      report += "| File | Complexity |\n";
      report += "|------|------------|\n";

      for (const item of complexities.slice(0, 30)) {
        report += `| ${item.file} | ${item.complexity} |\n`;
      }

      if (complexities.length > 30) {
        report += `\n*(${complexities.length - 30} more files...)*\n`;
      }

      report += "\n*Note: Complexity is estimated based on control flow keywords.*";

      return { content: [{ type: "text", text: report }] };
    }

    default:
      return { content: [{ type: "text", text: `Unknown tool: ${name}` }] };
  }
});

// Start server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

main().catch(console.error);
