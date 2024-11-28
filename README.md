## Alkalmazott mesterséges intelligencia modellek a gyakorlatban házi feladat

### Feladat: A31 - Dokumentáció generálása kódból LLM segítségével

### Neptun: Géró Kristóf (i0sk1n)

A projekt fő célja az volt, hogy egy olyan eszköz jöjjön létre, amely automatizálja a kód dokumentálását. Ehhez az OpenAI GPT-4o modellt használtam fel.

A fejlesztés során kihívást jelentett a megfelelő API hívások implementálása, illetve a promptok optimalizálása, hogy a kimenet minden fájltípus kiterjesztésre megfelelő legyen.

Sikerült létrehozni egy olyan, CLI-on keresztül hívható eszközt, amely egy bemeneti dokumentálatlan forráskód fájlt átalakít dokumentálttá. A rendszer a háttérben a GPT-4o modellt promptolja, amelyen az OpenAI API-n keresztül férek hozzá, ennek megfelelően a kód futtatásához az `OPENAI_API_KEY` környezeti változó megfelelő beállítása szükséges.

A feladat megoldása a `doccode.py` fájlban található.

A működő eszköz a következőképp néz ki:

![](https://github.com/ger0nymo/doccode/blob/main/recording.gif)
