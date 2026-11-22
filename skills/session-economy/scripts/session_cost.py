"""Where did the tokens go? usage: python3 session_cost.py ~/.claude/projects/<dir>/<session>.jsonl"""
import json, sys, collections
calls = {}; res = collections.Counter(); n = collections.Counter(); imgs = 0; u = collections.Counter(); api = 0
for line in open(sys.argv[1]):
    try: d = json.loads(line)
    except Exception: continue
    m = d.get('message') or {}
    if d.get('type') == 'assistant' and m.get('usage'):
        api += 1
        for k, v in m['usage'].items():
            if isinstance(v, int): u[k] += v
    c = m.get('content')
    if not isinstance(c, list): continue
    for b in c:
        if b.get('type') == 'tool_use': calls[b['id']] = b['name']
        if b.get('type') == 'tool_result':
            nm = calls.get(b.get('tool_use_id'), '?'); s = json.dumps(b.get('content')); res[nm] += len(s); n[nm] += 1
            imgs += s.count('"type": "image"')
print(f'API calls: {api}  images read: {imgs}')
for k in ('cache_read_input_tokens', 'cache_creation_input_tokens', 'output_tokens', 'input_tokens'): print(f'{k:30s} {u[k]:>14,}')
print('tool results (chars):')
for k, v in res.most_common(10): print(f'  {k:20s} calls={n[k]:5d} chars={v:>12,}')
