# Data Safety Checklist

## Purpose

Know what data is safe to share with AI tools. From Chapter 16.

## Data Classification

| Data Type | Guidance | Reason |
|-----------|----------|--------|
| Credentials | **NEVER** | API keys, passwords, tokens can be leaked |
| Customer PII | **NEVER** | Names, emails, addresses, IDs |
| Financial data | **NEVER without approval** | Requires special handling |
| Proprietary code | **CHECK POLICY** | Varies by organization |
| Internal docs | **GENERALLY NO** | Strategy, plans, unreleased work |
| Public code | **USUALLY FINE** | Open source, Stack Overflow |
| Personal projects | **YOUR CALL** | Consider your comfort level |

## Before Sharing, Ask:

1. Would I be comfortable if this appeared in a blog post?
2. Does this contain anything identifiable about customers or users?
3. Does this contain credentials, keys, or secrets?
4. Would a competitor learn something valuable from this?
5. Does my organization's policy allow this?

## Anonymization Techniques

### Variable Renaming

Before:
```
customer_payment_processor
StripeWebhookHandler
ACME_API_KEY
```

After:
```
service_a
ExternalAPIHandler
[REDACTED_KEY]
```

### Data Redaction

Before:
```json
{
  "api_key": "sk-live-abc123xyz",
  "customer_email": "john.doe@company.com",
  "amount": 150.00
}
```

After:
```json
{
  "api_key": "[REDACTED]",
  "customer_email": "user@example.com",
  "amount": 150.00
}
```

### Structure Preservation

Keep the shape, remove content:

Before: "Error processing payment for customer 12345: Card declined"
After: "Error processing payment for customer [ID]: [ERROR_MESSAGE]"

## Safe Problem Description Template

```
I have a [generic description] that receives [type of data].
When the handler receives [condition], it should:
1. [action 1]
2. [action 2]
3. [action 3]

Here is the structure (names changed, values redacted):

[paste anonymized code]

The problem: [describe without revealing specifics]
```

## Provider Policy Questions

Before using any AI tool for work, find answers to:

1. Is my data used for training?
2. How long is it retained?
3. Who might see it (human review)?
4. Does my organization have different terms?

## Quick Anonymization Checklist

Before pasting code or configs:

- [ ] No API keys or tokens
- [ ] No passwords or secrets
- [ ] No customer identifiers
- [ ] No internal system names (if sensitive)
- [ ] No email addresses (use example.com)
- [ ] No real IP addresses or hostnames
- [ ] No financial amounts (if sensitive)
