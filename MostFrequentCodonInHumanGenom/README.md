#  Finding the Most Frequent Codon Usage in the Human Genome

This project was developed as part of **Computational Biology** studies at **Ege University, Computer Engineering Department**. It aims to identify which codons are used most frequently in the human genome and their corresponding amino acids.

---

## 🇺🇸 [ENGLISH]

###  Project Overview
Analyzing genetic code frequency is a fundamental task in bioinformatics to understand codon preference during amino acid synthesis. This software efficiently processes large-scale genomic data in FASTA format to report the top 5 most frequent codons.

###  Algorithm & Strategy
Since human genome files are enormous (often gigabytes in size), loading the entire file into RAM would cause system crashes. To solve this, a **"Line-by-Line Buffering"** strategy is used:
* **Safe Reading:** The file is opened safely and read one line at a time.
* **Data Cleaning:** Invisible characters like line breaks are removed using `.strip()`.
* **Header Handling:** The algorithm checks for the `>` character to detect the start of a new gene.
* **Sequence Processing:** DNA sequences are accumulated in a buffer and processed into valid codons (ignoring 'N' or invalid lengths).

### 📊 Results
Analysis on the `Homo_sapiens.GRCh38.cds.all.fa` dataset yielded the following results:

| Rank | Codon | Amino Acid | Count |
| :--- | :--- | :--- | :--- |
| 1 | **GAG** | Glu (Glutamic Acid) | 1,433,362 |
| 2 | **CTG** | Leu (Leucine) | 1,373,164 |
| 3 | **CAG** | Gln (Glutamine) | 1,256,653 |
| 4 | **AAG** | Lys (Lysine) | 1,141,269 |
| 5 | **GAA** | Glu (Glutamic Acid) | 1,096,666 |

---

## 🇹🇷 [TURKISH]

###  Proje Özeti
Genetik kod frekansının analizi, amino asit sentezi sırasında kodon tercihlerini anlamak için biyoinformatikte temel bir görevdir. Bu yazılım, FASTA formatındaki büyük ölçekli genom verilerini verimli bir şekilde işleyerek en sık rastlanan 5 kodonu raporlar.

###  Algoritma ve Strateji
İnsan genom dosyaları devasa boyutlarda olduğu için, dosyanın tamamını RAM'e yüklemek sistem çökmelerine neden olur. Bu sorunu çözmek için **"Satır Satır Tamponlama"** stratejisi uygulanmıştır:
* **Güvenli Okuma:** Dosya güvenli bir şekilde açılır ve her seferinde tek bir satır okunur.
* **Veri Temizleme:** Satır sonu karakterleri gibi görünmez karakterler `.strip()` ile temizlenir.
* **Başlık Yönetimi:** Yeni bir genin başlangıcını tespit etmek için `>` karakteri kontrol edilir.
* **Sekans İşleme:** DNA dizileri bir tamponda toplanır ve geçerli kodonlara dönüştürülür ('N' içerenler veya hatalı uzunluklar hariç tutulur).

### 📊 Sonuçlar
`Homo_sapiens.GRCh38.cds.all.fa` veri seti üzerindeki analiz şu sonuçları vermiştir:

| Sıra | Kodon | Amino Asit | Frekans |
| :--- | :--- | :--- | :--- |
| 1 | **GAG** | Glu (Glutamik Asit) | 1,433,362 |
| 2 | **CTG** | Leu (Lösin) | 1,373,164 |
| 3 | **CAG** | Gln (Glutamin) | 1,256,653 |
| 4 | **AAG** | Lys (Lizin) | 1,141,269 |
| 5 | **GAA** | Glu (Glutamik Asit) | 1,096,666 |

---

**Author / Hazırlayan:** Yunus Can Duman  
**Date / Tarih:** 19.02.2026
