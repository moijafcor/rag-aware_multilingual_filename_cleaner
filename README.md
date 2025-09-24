# 🧹RAG-aware Multilingual Filename Cleaner for RAG Pipelines

A Python utility for **cleaning and normalizing filenames** in bulk, designed with **RAG (Retrieval-Augmented Generation)** in mind to enrich LLMs (Large Language Models) workflows.  

Unlike aggressive sanitizers that strip out context, this tool preserves **semantic richness** (e.g., subject, grade, language) while ensuring filenames remain **portable and queryable**.  

---

## ✨ Features

- **Dry-run by default** → see what changes would happen without renaming.  
- **Semantic preservation** → keeps meaningful tokens like *Matemática*, *Francés*, *5to Primaria*.  
- **Unicode-aware** → accents (`é`, `ñ`, `ç`) preserved unless you force ASCII mode.  
- **Safe cleaning**:
  - Spaces → underscores
  - Removes problematic symbols (`°`, `?`, `!`, etc.)
  - Collapses multiple underscores
  - Strips leading/trailing separators
- **Collision handling** → automatically appends suffixes (`_1`, `_2`) if cleaned names clash.  
- **Portable mode** → optional `--ascii` flag converts filenames to ASCII-only.  
- **Extensible** → easily adapt rules for your ingestion pipeline.

---

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/your-username/filename-cleaner.git
cd filename-cleaner
```

Make the script executable:

```bash
chmod +x clean_filenames.py
```

Or just run with Python:

```bash
python3 clean_filenames.py
```

--- 

## 🚀 Usage

Dry-run (default)

Preview how files would be renamed:

```bash
python3 clean_filenames.py /path/to/files
```

Example output:

```bash
5Secundaria_Lenguas extranjeras Francés 5°_enriched.jsonl  
 →  5Secundaria_Lenguas_extranjeras_Francés_5_enriched.jsonl
```

Apply changes

Actually rename the files:

```bash
python3 clean_filenames.py /path/to/files --apply
```

ASCII-only mode

Normalize accents to plain letters for maximum portability:

```bash
python3 clean_filenames.py /path/to/files --ascii
```

Example:

```bash
5p_Educación_Artística_5_Cuadernillo_enriched.jsonl  
 →  5p_Educacion_Artistica_5_Cuadernillo_enriched.jsonl
```

🛠 Options

| Flag        | Description                                                   |
| ----------- | ------------------------------------------------------------- |
| `--apply`   | Perform the actual renaming (default: dry-run).               |
| `--ascii`   | Strip accents and normalize to ASCII (e.g. `é → e`, `ñ → n`). |
| `directory` | Target directory (default: `.`).                              |

---

## 📚 Best Practices for RAG Pipelines

- Keep semantic tokens: Filenames often carry key metadata (grade, subject, language).
- Unicode-safe unless necessary: Retain accents unless you need strict ASCII.
- Consistent separators: Underscores _ make parsing and downstream tokenization easier.
- Metadata extraction (optional): Consider pairing this with a parser that extracts fields from filenames into structured JSON for richer retrieval.

---

## 🧪 Example Before & After

Input files

```txt
'5Secundaria_Lenguas extranjeras Francés 5°_enriched.jsonl'
'5p_Educación Artística 5° Cuadernillo_enriched.jsonl'
```

Cleaned (Unicode mode)

```txt
5Secundaria_Lenguas_extranjeras_Francés_5_enriched.jsonl
5p_Educación_Artística_5_Cuadernillo_enriched.jsonl
```

Cleaned (ASCII mode)

```txt
5Secundaria_Lenguas_extranjeras_Frances_5_enriched.jsonl
5p_Educacion_Artistica_5_Cuadernillo_enriched.jsonl
```

---

## 📝 License

MIT License — feel free to use, adapt, and share.

## 🤝 Contributing

Pull requests welcome! Ideas for improvements:

- Add a --json-metadata option to export parsed metadata alongside each file.
- More configurable cleaning rules (custom regex or stopwords).
- Batch logging and undo support.

---

## 🙏 Acknowledgments

This project was developed with the assistance of [ChatGPT (OpenAI GPT-5)](https://openai.com/chatgpt), which helped design the filename cleaning logic and documentation.

