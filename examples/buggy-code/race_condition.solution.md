# Solution: Race Conditions

## Bug 1: Non-atomic inventory update

**Problem**: Read and write are separate operations with await in between.

```javascript
// Buggy
const currentStock = inventory[item];
await someOperation();
inventory[item] = currentStock - quantity;

// Fixed: Use atomic operation or lock
async function purchaseItem(item, quantity) {
  // Option 1: Database transaction
  return await db.transaction(async (tx) => {
    const stock = await tx.get(`inventory:${item}`);
    if (stock >= quantity) {
      await tx.set(`inventory:${item}`, stock - quantity);
      return { success: true };
    }
    return { success: false };
  });

  // Option 2: Mutex lock
  await inventoryLock.acquire();
  try {
    // ... atomic operation
  } finally {
    inventoryLock.release();
  }
}
```

## Bug 2: Non-atomic counter

**Problem**: `read, increment, write` can interleave.

```javascript
// Buggy
const orderId = orderCounter;
orderCounter = orderCounter + 1;

// Fixed: Atomic increment
const orderId = await atomicIncrement('orderCounter');

// Or use database sequence
const orderId = await db.query('SELECT nextval("order_seq")');
```

## Bug 3: Missing await in loop

**Problem**: Promises pushed to array, not resolved values.

```javascript
// Buggy
for (const order of orders) {
  results.push(processOrder(order));  // Pushes promise
}
return results;  // Returns array of promises

// Fixed
for (const order of orders) {
  results.push(await processOrder(order));  // Pushes value
}

// Or parallel execution
return await Promise.all(orders.map(processOrder));
```

## Bug 4: forEach with async

**Problem**: forEach doesn't await async callbacks.

```javascript
// Buggy
items.forEach(async (item) => {
  const result = await updatePrice(item);
  updates.push(result);
});
return updates;  // Empty!

// Fixed: Use for...of
for (const item of items) {
  updates.push(await updatePrice(item));
}

// Or parallel
return await Promise.all(items.map(updatePrice));
```

## Lessons

1. **Identify atomic boundaries**: What operations must complete together?
2. **Be suspicious of await in loops**: Each await is a potential interleaving point
3. **forEach is sync**: Use for...of or Promise.all for async iteration
4. **Test with concurrency**: Sequential tests don't find race conditions

## AI Debugging Tips

When debugging async issues:

1. Ask AI to "trace the execution order with multiple concurrent calls"
2. Request identification of "points where state can change during await"
3. Ask for "thread-safe" or "atomic" alternatives
