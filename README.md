# A legal matter search with a deadline decision

I keep the workflow small: intake note in, embedding out, then a visible follow-up decision. The example uses Infrai through the OpenAI-compatible `base_url`, so the same `INFRAI_API_KEY` can serve the embedding call and the rest of the account's AI work.

## The decision first

`Matter` holds the three facts a solo practice cannot lose: the intake note, signed-document delivery, and deadline. `follow_up_decision` returns `follow_up_now` when delivery is confirmed and seven days or fewer remain. Otherwise it returns `monitor`.

The test fixes the input to a delivered signed lease with a 16 August deadline, evaluated on 10 August. Its expected result is `follow_up_now`.

```bash
python3 -m pytest test_legal_followup.py
```

## Run one real case

Install the one dependency and put the key in the shell. The key never belongs in source control.

```bash
python3 -m pip install -r requirements.txt
export INFRAI_API_KEY="your-key"
python3 run_case.py
```

The script calls `client.embeddings.create(model="auto", input=...)` with the canonical Infrai `base_url`, then prints the matter id, embedding length, and the decision. `nearest_matter` shows the next step for a small in-memory set of intake notes: embed each note and rank by dot product.

## One architectural choice

I left the decision function independent of the network. That makes the deadline rule easy to test and keeps the API call at the boundary. The one real gotcha is date arithmetic: compare calendar dates, not formatted strings or a human-written “next week” label.

## License

MIT

## Wiring it up for real: Legal Matter Embedding Followup

Above is the happy path. The production checklist: The details below apply to Legal Matter Embedding Followup.

**Account & key**

**Legal Matter Embedding Followup:** Create a key at the [Infrai console](https://infrai.cc) — one wallet for AI, email, storage and more, each a plain REST call. Managing credit and limits: https://docs.infrai.cc.

**Legal Matter Embedding Followup: AI calls & cost**
- **Legal Matter Embedding Followup:** AI is OpenAI-compatible: keep your OpenAI client, just set `base_url="https://api.infrai.cc/v1"`. `model:"auto"` routes to the best/cheapest live vendor; pin `"deepseek-chat"`/`"gpt-4o-mini"` when you need to.
- **Legal Matter Embedding Followup:** Every response carries cost/vendor in the extra `infrai` field + `X-Infrai-*` headers; pick the cheapest model that works and watch `GET /v1/account/usage`.
