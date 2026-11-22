# Claude Skills Hub

مهارات لـ Claude لإنتاج أسرع وأعلى كفاءة في الثري دي، ويونيتي، والواقع الافتراضي (Meta Quest)، والفن الضوئي.

- **12 مهارة من تأليفنا** مستخلصة من مشروع حقيقي، في `skills/`.
- **252 مهارة مختارة من GitHub** برخص مفتوحة، في `vendor/`، ومع كل مصدر رخصته و`SOURCE.md`.
- **دراسة الاستهلاك**: `ANALYSIS-AR.md` (أين ذهبت التوكينز وكيف نوفّرها).
- **الفهرس**: `CATALOG.md` (كل مهارة ولماذا، وأدوات مفيدة نشير إليها فقط).

## التثبيت
كل مهارة مثبّتة يُحمَّل وصفها في **كل** جلسة، فثبّت الحزم التي تحتاجها فقط:
```bash
git clone <رابط هذا المستودع> && cd claude-skills-hub
./install.sh list                # عرض الحزم
./install.sh core unity          # المقترح لمشروع يونيتي للنظارة
```
الحزم: `core` · `unity` · `blender` · `blender-extra` · `webxr` · `vfx` · `godot` · `ai3d` · `tokens` · `optional`.
تُثبَّت في `~/.claude/skills`، أو في مجلد تختاره بـ `DEST=... ./install.sh core`.

## أهم أداة لمشروع يونيتي
مهارة `unity-mcp-skill` تعمل مع **MCP for Unity** (CoplayDev/unity-mcp): يتحكم Claude في محرر يونيتي على جهازك مباشرة (ينشئ المشاهد والمواد والسكربتات)، بدل أن تضغط الأزرار بنفسك. تحتاج تثبيتها على الكمبيوتر مرة واحدة مع Claude Code أو Claude Desktop هناك.
