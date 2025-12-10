/**
 * Race Condition Example
 *
 * This code has async/await issues that cause race conditions.
 * Use AI debugging to identify the timing problems.
 *
 * Exercise: Find why the counter is wrong and orders may be lost.
 */

// Simulated database
let inventory = { widget: 10 };
let orderCounter = 0;

/**
 * Bug: Non-atomic read-modify-write creates race condition
 */
async function purchaseItem(item, quantity) {
  // Check inventory
  const currentStock = inventory[item];

  if (currentStock >= quantity) {
    // Simulate network delay
    await new Promise((resolve) => setTimeout(resolve, 10));

    // Bug: inventory may have changed during the await
    inventory[item] = currentStock - quantity;
    return { success: true, remaining: inventory[item] };
  }

  return { success: false, reason: "Insufficient stock" };
}

/**
 * Bug: Counter increment isn't atomic
 */
async function createOrder(items) {
  // Bug: read and write are separate operations
  const orderId = orderCounter;
  orderCounter = orderCounter + 1;

  // Simulate processing
  await new Promise((resolve) => setTimeout(resolve, 5));

  return {
    id: orderId,
    items: items,
    timestamp: Date.now(),
  };
}

/**
 * Bug: Missing await causes silent failures
 */
async function processOrderBatch(orders) {
  const results = [];

  for (const order of orders) {
    // Bug: push happens before async operation completes
    results.push(processOrder(order));
  }

  // Bug: returning promises, not resolved values
  return results;
}

async function processOrder(order) {
  await new Promise((resolve) => setTimeout(resolve, 10));
  return { orderId: order.id, status: "processed" };
}

/**
 * Bug: forEach doesn't handle async properly
 */
async function updateAllPrices(items, multiplier) {
  const updates = [];

  // Bug: forEach callback is async but forEach doesn't await
  items.forEach(async (item) => {
    const result = await updatePrice(item, multiplier);
    updates.push(result);
  });

  // Bug: returns immediately, before any updates complete
  return updates;
}

async function updatePrice(item, multiplier) {
  await new Promise((resolve) => setTimeout(resolve, 5));
  return { item: item, newPrice: item.price * multiplier };
}

// Demonstration of race conditions
async function main() {
  console.log("=== Race Condition Demonstrations ===\n");

  // Demo 1: Inventory race condition
  console.log("1. Inventory Race Condition");
  console.log(`   Starting inventory: ${inventory.widget} widgets`);

  // Simulate 5 concurrent purchases of 3 widgets each
  const purchases = [];
  for (let i = 0; i < 5; i++) {
    purchases.push(purchaseItem("widget", 3));
  }

  const purchaseResults = await Promise.all(purchases);
  console.log(`   Results: ${purchaseResults.filter((r) => r.success).length} successful`);
  console.log(`   Final inventory: ${inventory.widget} widgets`);
  console.log(`   Expected: Only 3 should succeed (10/3 = 3), inventory should be 1`);
  console.log();

  // Demo 2: Order counter race condition
  console.log("2. Order Counter Race Condition");
  const orders = [];
  for (let i = 0; i < 5; i++) {
    orders.push(createOrder([`item-${i}`]));
  }

  const orderResults = await Promise.all(orders);
  const orderIds = orderResults.map((o) => o.id);
  console.log(`   Order IDs: ${orderIds}`);
  console.log(`   Expected: [0, 1, 2, 3, 4], may have duplicates`);
  console.log();

  // Demo 3: forEach async bug
  console.log("3. forEach Async Bug");
  const items = [
    { name: "A", price: 10 },
    { name: "B", price: 20 },
  ];
  const priceUpdates = await updateAllPrices(items, 1.5);
  console.log(`   Updates returned: ${priceUpdates.length}`);
  console.log(`   Expected: 2, but returns 0 (empty array)`);
}

main().catch(console.error);
