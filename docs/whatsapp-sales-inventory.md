# WhatsApp sales and inventory agent

A Make.com prototype for requesting sales reports, stock summaries, and product availability over WhatsApp. It uses Twilio for messaging, Make AI Agents for intent extraction, and Google Sheets for sales and inventory data.

## Workflow

1. Twilio delivers an inbound WhatsApp message to a Make webhook.
2. In the intake scenario, Make AI Agents extracts the intent, date range, and product. Make parses the JSON and sends the structured request to a second scenario over HTTP.
3. A router in the reporting scenario directs the request to the sales or inventory branch. The sales branch filters rows by date and sums quantity and total. The inventory branch looks up stock by product.
4. Twilio delivers a WhatsApp reply with the results.

## Example request

This illustrative payload uses a synthetic name and the reserved fictional phone range.

```json
{
  "user_number": "whatsapp:+12025550104",
  "profile_name": "Demo User",
  "raw_message": "How much did we sell from November 19 to November 20?",
  "intent": "sales_report",
  "start_date": "2026-11-19",
  "end_date": "2026-11-20",
  "product": null
}
```

## Sample data

Import [sales.csv](../examples/whatsapp-sales-inventory/sales.csv) and [inventory.csv](../examples/whatsapp-sales-inventory/inventory.csv) into separate Google Sheets tabs. Both files contain synthetic data, and prices are in NGN.

For an inclusive date range of November 19–20, 2026, the sales sample should return **6 units** and **₦45,900**. A stock lookup for **Classic Notebook** should return **24 units**. The sample also includes a low-stock item and an out-of-stock item.

The prototype used a normalized `Date_ISO` field for date filtering in its sales history. Keep dates in `YYYY-MM-DD` and make sure the sheet and Make use the same date field and interpretation. Sum numeric quantity and total columns before formatting the currency in the reply.

This walkthrough and sample data describe the workflow. An importable Make blueprint is pending.
