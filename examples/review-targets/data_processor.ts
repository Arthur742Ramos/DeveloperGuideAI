/**
 * Data Processor Review Target
 *
 * Review this code for:
 * - Error handling patterns
 * - Type safety
 * - Resource management
 * - Code organization
 *
 * Exercise: Use the code-review prompt to analyze this file.
 */

interface DataRecord {
  id: number;
  value: string;
  timestamp: Date;
}

interface ProcessResult {
  processed: number;
  failed: number;
  errors: string[];
}

// Issue: Any type usage
async function fetchData(url: string): Promise<any> {
  const response = await fetch(url);
  // Issue: No error handling for non-200 responses
  return response.json();
}

// Issue: Inconsistent error handling
async function processRecords(records: DataRecord[]): Promise<ProcessResult> {
  let processed = 0;
  let failed = 0;
  const errors: string[] = [];

  for (const record of records) {
    try {
      // Issue: Side effect in processing function
      console.log(`Processing ${record.id}`);

      // Issue: No validation of record structure
      const result = await transformRecord(record);

      // Issue: Mutating input data
      (record as any).processed = true;
      (record as any).result = result;

      processed++;
    } catch (e) {
      // Issue: Swallowing error details
      failed++;
      errors.push(`Failed to process record ${record.id}`);
    }
  }

  return { processed, failed, errors };
}

async function transformRecord(record: DataRecord): Promise<string> {
  // Issue: Magic number
  if (record.value.length > 100) {
    throw new Error("Value too long");
  }

  // Issue: No null check
  return record.value.toUpperCase();
}

// Issue: Callback-style mixed with promises
function loadAndProcess(
  url: string,
  callback: (err: Error | null, result?: ProcessResult) => void
) {
  fetchData(url)
    .then((data) => {
      // Issue: No type validation of fetched data
      return processRecords(data.records);
    })
    .then((result) => {
      callback(null, result);
    })
    .catch((err) => {
      callback(err);
    });
}

// Issue: No cleanup of interval
function startPolling(url: string, intervalMs: number) {
  // Issue: No way to stop polling
  setInterval(async () => {
    try {
      const data = await fetchData(url);
      await processRecords(data.records);
    } catch (e) {
      // Issue: Silent failure
    }
  }, intervalMs);
}

// Issue: Race condition in cache
const cache: Map<string, DataRecord[]> = new Map();

async function getCachedData(key: string): Promise<DataRecord[]> {
  if (!cache.has(key)) {
    // Issue: Multiple simultaneous calls will all fetch
    const data = await fetchData(`/api/data/${key}`);
    cache.set(key, data);
  }
  return cache.get(key)!; // Issue: Non-null assertion
}

// Issue: No timeout handling
async function fetchWithRetry(url: string, maxRetries: number): Promise<any> {
  let lastError: Error | undefined;

  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fetchData(url);
    } catch (e) {
      lastError = e as Error;
      // Issue: No exponential backoff
      await new Promise((r) => setTimeout(r, 1000));
    }
  }

  throw lastError;
}

// Issue: Exporting mutable state
export { cache, fetchData, processRecords, startPolling, getCachedData };
