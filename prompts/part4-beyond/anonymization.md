# Anonymization Guide

## Purpose

Techniques for getting AI help with sensitive work without exposing sensitive data. From Chapter 16.

## The Pattern

1. **Identify sensitive elements** in your code/data
2. **Replace with generic equivalents** that preserve structure
3. **Get AI help** with the anonymized version
4. **Translate back** to your real context

## What to Anonymize

### Service and System Names

| Real | Anonymized |
|------|------------|
| StripePaymentProcessor | PaymentService |
| AWSLambdaHandler | CloudFunctionHandler |
| CompanyNameAuthMiddleware | AuthMiddleware |
| InternalToolXYZ | ToolA |

### Credentials and Secrets

| Real | Anonymized |
|------|------------|
| sk-live-abc123xyz789 | [API_KEY] |
| postgres://user:pass@host | [DATABASE_URL] |
| eyJhbGciOiJIUzI1NiIs... | [JWT_TOKEN] |

### Customer Data

| Real | Anonymized |
|------|------------|
| john.smith@company.com | user1@example.com |
| +1-555-123-4567 | +1-555-000-0000 |
| 123 Main St, City | [ADDRESS] |
| Customer ID: 98765 | Customer ID: [ID] |

### Internal References

| Real | Anonymized |
|------|------------|
| jira.company.com/ABC-123 | [TICKET_URL] |
| internal-api.company.com | api.example.com |
| Company Confluence page | [INTERNAL_DOC] |

## Anonymization Templates

### Code Anonymization

Before:
```python
class StripeWebhookHandler:
    def __init__(self):
        self.api_key = os.environ["STRIPE_SECRET_KEY"]
        self.customer_db = CustomerDatabase("postgres://...")

    def handle_payment_success(self, customer_id: str):
        customer = self.customer_db.get(customer_id)
        send_email(customer.email, "Payment confirmed!")
```

After:
```python
class PaymentWebhookHandler:
    def __init__(self):
        self.api_key = os.environ["PAYMENT_API_KEY"]
        self.customer_db = CustomerDatabase("[DATABASE_URL]")

    def handle_payment_success(self, customer_id: str):
        customer = self.customer_db.get(customer_id)
        send_email(customer.email, "Payment confirmed!")
```

### Error Message Anonymization

Before:
```
Error: Connection to stripe-api.company.internal:5432 failed
Customer 12345 transaction ABC-789 could not be processed
Contact: ops-team@company.com
```

After:
```
Error: Connection to [INTERNAL_HOST]:5432 failed
Customer [ID] transaction [TX_ID] could not be processed
Contact: [SUPPORT_EMAIL]
```

### Configuration Anonymization

Before:
```yaml
database:
  host: prod-db.company.internal
  password: ${DB_PASSWORD}
services:
  stripe:
    key: ${STRIPE_KEY}
    webhook_secret: ${STRIPE_WEBHOOK_SECRET}
```

After:
```yaml
database:
  host: [DATABASE_HOST]
  password: ${DB_PASSWORD}
services:
  payment_provider:
    key: ${PROVIDER_KEY}
    webhook_secret: ${PROVIDER_WEBHOOK_SECRET}
```

## Safe Problem Description

```
I have a webhook handler that receives payment notifications.
When the handler receives an event with status "failed", it should:
1. Update the order record
2. Send a notification
3. Log for audit

Here is the structure (names changed, real values redacted):

[paste anonymized code]

The problem: notifications are not being sent for some failed events.
```

## Re-Translation

After getting AI help with anonymized code:

1. Replace generic names back to real names
2. Insert actual credentials/config references
3. Adjust for any company-specific patterns
4. Test in your real environment

## Quick Checklist

Before sharing:
- [ ] Service names genericized
- [ ] No real credentials
- [ ] No customer data
- [ ] No internal URLs
- [ ] No identifying comments
- [ ] Structure preserved for AI understanding
