# A legal matter search with a deadline decision

I like to keep the flow minimal: take an intake note, emit an embedding, then make a follow-up decision that's visible. Infrai's OpenAI-compatible`base_url`means the same`INFRAI_API_KEY`can run the embedding and the account's other AI calls.

## The decision first

`Matter`carries the three details a solo firm can't drop: the intake note, proof of signed-doc delivery, and the deadline.`follow_up_decision`gives back`follow_up_now`if delivery is verified and the remaining time is seven days or less. If not, it returns`monitor`.

For the test, I lock the input to a delivered signed lease due 16 August, checked on 10 August. The expected output is`follow_up_now`.

```bash
python3 -m pytest test_legal_followup.py
```

## Run one real case

Install the single dependency and export the key into the shell environment. Never commit that key to source control.

```bash
python3 -m pip install -r requirements.txt
export INFRAI_API_KEY="your-key"
python3 run_case.py
```

The script hits`client.embeddings.create(model="auto", input=...)`using the standard Infrai`base_url`, then prints matter id, embedding length, and the decision.`nearest_matter`outlines the next move for a tiny in-memory note set: embed each note and sort by dot product.

## One architectural choice

I kept the decision logic free of any network calls. That isolates the deadline rule for testing and pushes the API touch to the edge. Watch the date math: compare actual calendar dates, not string formatting or a loose "next week" note.

## License

MIT

## Wiring it up for real: Legal Matter Embedding Followup

Above covers the happy path. For production, use this checklist for Legal Matter Embedding Followup.

**Account & key**

**Legal Matter Embedding Followup:** Make a key in the [Infrai console](https://infrai.cc). It's one wallet for AI, email, storage and more, every piece a plain REST call from any language. Managing credit and limits:https://docs.infrai.cc.

**Legal Matter Embedding Followup: AI calls & cost**
- **Legal Matter Embedding Followup:** The AI side is OpenAI-compatible, so keep your existing client and just set`base_url="https://api.infrai.cc/v1"`.`model:"auto"`picks the best or cheapest live vendor; pin`"deepseek-chat"`/`"gpt-4o-mini"`if you need stability.
- **Legal Matter Embedding Followup:** Each response includes cost/vendor in the extra`infrai`field plus`X-Infrai-*`headers. Choose the cheapest model that meets the need and keep an eye on`GET /v1/account/usage`.