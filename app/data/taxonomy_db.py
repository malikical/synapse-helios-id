"""
SYNAPSE HELIOS ID - Comprehensive Indonesian AI Taxonomy Database
Taksonomi & Klasifikasi Arsitektur Kecerdasan Buatan Terkini
"""
from typing import List
from app.models.ai_taxonomy import AICategory, AITypeItem, ArchitecturalFeature, BenchmarkMetric

AI_TAXONOMY_DATA: List[AICategory] = [
    AICategory(
        id="reasoning-test-time",
        numeral="01",
        name="Model Penalaran Mendalam & Komputasi Inferensi",
        english_name="Reasoning & Test-Time Compute Models",
        tagline="Penskalaan komputasi inferensi melalui rantai pemikiran tersembunyi dan pencarian pohon berbasis penguatan (RL).",
        overview=(
            "Model Penalaran (Reasoning Models) merepresentasikan lompatan paradigma terbesar pasca era LLM murni. "
            "Jika model klasik hanya mengandalkan penskalaan parameter saat pre-training (Kaplan/Chinchilla scaling laws), "
            "model penalaran modern mengalokasikan siklus komputasi dinamis saat inferensi (Test-Time Compute Scaling) "
            "menggunakan Hidden Chain-of-Thought (CoT) dan Reinforcement Learning with Search (RL + PRM)."
        ),
        paradigm_shift="Pergeseran dari 'Pre-training Compute Dominated' menuju 'Test-Time Compute Scalability'.",
        items=[
            AITypeItem(
                id="test-time-search-prm",
                category_id="reasoning-test-time",
                title="Test-Time Compute & Hidden CoT Engine",
                tagline="Eksplorasi pohon solusi tersembunyi dengan verifikasi langkah per langkah.",
                badge="SOTA REASONING",
                description=(
                    "Sistem inferensi yang menghasilkan ribuan token penalaran internal (hidden thinking tokens) "
                    "sebelum merumuskan output final. Mengintegrasikan Process Reward Models (PRM) yang memberikan umpan balik "
                    "pada setiap atomik langkah logika matematika/kode, bukan sekadar Outcome Reward Models (ORM)."
                ),
                deep_dive=(
                    "Pada model seperti OpenAI o1/o3 dan DeepSeek-R1, mekanisme penalaran dilatih menggunakan "
                    "Reinforcement Learning berskala besar tanpa supervised fine-tuning (SFT) yang berat di tahap awal (Pure RL). "
                    "Model secara mandiri menemukan strategi 'backtracking', 'self-correction', 'hypothesis testing', "
                    "dan 'branch pruning' saat menemui jalan buntu dalam pembuktian formal matematika atau debugging kode biner."
                ),
                key_mechanisms=[
                    "Hidden Chain-of-Thought (CoT) tokenization dengan alokasi budget komputasi fleksibel.",
                    "Process Reward Models (PRM) untuk evaluasi probabilitas kebenaran tiap sub-langkah.",
                    "Monte Carlo Tree Search (MCTS) & Guided Beam Search terintegrasi saat generasi token.",
                    "Self-Correction & Backtracking otomatis tanpa intervensi pengguna luar."
                ],
                pioneer_models=["OpenAI o1", "OpenAI o3 / o3-mini", "DeepSeek-R1", "Alibaba QwQ-32B-Preview"],
                architectural_features=[
                    ArchitecturalFeature(
                        title="Formulasi Penskalaan Komputasi Uji (Test-Time Scaling)",
                        detail="Peningkatan akurasi berbanding lurus dengan logaritma komputasi pencarian saat inferensi:",
                        code_or_formula=r"Performance(Acc) ∝ f(N_parameters, D_tokens, C_test_compute_FLOPs)"
                    ),
                    ArchitecturalFeature(
                        title="Process-Supervised Value Function",
                        detail="Fungsi nilai atomik menghitung reward per langkah logika (k):",
                        code_or_formula=r"R_{PRM} = \sum_{k=1}^{K} \gamma^k \cdot \sigma(W_v \cdot h_k)"
                    )
                ],
                benchmarks=[
                    BenchmarkMetric(name="AIME 2024 (Math Olympiad)", score="83.3% - 91.8%", baseline="GPT-4o: 13.4%", description="Kemampuan penyelesaian soal matematika tingkat olimpiade internasional."),
                    BenchmarkMetric(name="Codeforces Elo", score="1807 - 2088 (Top 96-98%)", baseline="Human Grandmaster: 2200+", description="Peringkat kompetitif pemrograman algoritma dinamis."),
                    BenchmarkMetric(name="GPQA Diamond", score="78.4% - 87.7%", baseline="PhD Human Expert: ~65%", description="Pertanyaan sains tingkat doktoral (Fisika, Kimia, Biologi).")
                ],
                computational_complexity="O(T_think * N_heads * D_model) per kueri kompleks (Variabel depend pada kedalaman CoT)",
                hardware_affinity="High-Memory Bandwidth Cluster (H100/H200/B200 SXM5) dengan VRAM FP8/BF16 besar",
                use_cases=[
                    "Pembuktian teorema matematika dan verifikasi formal perangkat lunak (Coq/Lean).",
                    "Audit kerentanan keamanan kode biner dan eksploitasi kriptografi zero-day.",
                    "Sintesis rute kimia organik dan perancangan obat molekuler berpresisi tinggi."
                ],
                risk_and_alignment="Risiko Deceptive Alignment selama proses CoT internal; membutuhkan CoT Readout Monitors & Sandboxing."
            )
        ]
    ),
    AICategory(
        id="omni-modal-frontier",
        numeral="02",
        name="Model Fondasi Omni-Modal Lintas Domain",
        english_name="Omni-Modal & Frontier Foundation Models",
        tagline="Pemrosesan natif terpadu multi-modalitas (suara, video, teks, spasial) dengan jendela konteks masif.",
        overview=(
            "Model Omni-modal menghilangkan arsitektur 'cascaded pipe' kuno (seperti Whisper -> LLM -> ElevenLabs) "
            "dan menggantikannya dengan tokenizer representasi laten terpadu. Model 'mendengar' gelombang audio mentah, "
            "'melihat' frame video secara kontinu, dan merespons secara real-time dengan latensi sub-300ms."
        ),
        paradigm_shift="Integrasi end-to-end multi-sensorik dalam satu matriks bobot tensor tunggal.",
        items=[
            AITypeItem(
                id="native-omni-foundation",
                category_id="omni-modal-frontier",
                title="Frontier Native Omni-Modal Architecture",
                tagline="Pemrosesan audio-to-audio, video real-time, dan penalaran multimodal simultan.",
                badge="NATIVE MULTIMODAL",
                description=(
                    "Arsitektur fondasi generasi baru yang memetakan spektrum elektromagnetik (citra/video), "
                    "gelombang akustik (audio), dan struktur simbolik (teks) ke dalam shared latent manifold yang sama."
                ),
                deep_dive=(
                    "Sistem seperti Google Gemini 2.0 (Flash & Pro), Claude 3.5/3.7 Sonnet, dan GPT-4o tidak lagi melakukan OCR "
                    "atau transkripsi perantara. Hal ini memungkinkan model menangkap modulasi nada bicara, jeda emosional, "
                    "aksen daerah, oklusi spasial 3D dari kamera streaming, serta konteks hingga 2 juta - 10 juta token secara stabil."
                ),
                key_mechanisms=[
                    "Native Continuous Audio & Video Tokenizers (Continuous Latent Representation).",
                    "Any-to-Any Streaming Inference dengan latensi interupsi (barge-in) interaktif < 250ms.",
                    "Extreme In-Context Learning (Jendela konteks 2M - 10M+ tokens dengan Needle-in-Haystack > 99.8%).",
                    "Interleaved Multi-modal Generation (Mampu menghasilkan teks berdampingan dengan gambar & audio terkoordinasi)."
                ],
                pioneer_models=["Google Gemini 2.0 Flash / Pro", "Claude 3.7 Sonnet (Hybrid Reasoning)", "OpenAI GPT-4o"],
                architectural_features=[
                    ArchitecturalFeature(
                        title="Unified Cross-Modal Attention",
                        detail="Matriks atensi memproyeksikan token visual (v), audio (a), dan teks (t) secara simultan:",
                        code_or_formula=r"Attention(Q, K, V) = \text{softmax}\left(\frac{Q_{m} K_{m}^T}{\sqrt{d_k}}\right) V_{m}, \quad m \in \{txt, vis, aud\}"
                    ),
                    ArchitecturalFeature(
                        title="Rotary Position Embedding (RoPE) Multi-Dimensi",
                        detail="Mendukung koordinat temporal frame video dan spasial piksel 2D/3D:",
                        code_or_formula=r"R_{\Theta, m}^{2D/3D} = \text{diag}(R_{\theta_t}, R_{\theta_x}, R_{\theta_y})"
                    )
                ],
                benchmarks=[
                    BenchmarkMetric(name="MMMU (Multimodal Multidiscipline)", score="70.2% - 77.8%", baseline="GPT-4V: 56.8%", description="Penalaran visual tingkat perguruan tinggi lintas 30 disiplin ilmu."),
                    BenchmarkMetric(name="Video-MME", score="82.4% - 88.1%", baseline="Gemini 1.5: 75.0%", description="Pemahaman video durasi panjang (hingga 2 jam) dengan kueri temporal kompleks."),
                    BenchmarkMetric(name="Needle In A Haystack (2M Context)", score="99.9% Retrieval", baseline="RAG Standard: 82.0%", description="Presisi temu kembali fakta terisolasi dalam 2 juta token.")
                ],
                computational_complexity="Linear FlashAttention-3 / KV-Cache Compression (RingAttention / PagedAttention)",
                hardware_affinity="TPU v5p / TPU v6e Pod Slices, NVIDIA H100 NVLink Clusters dengan RoCE v2 Network",
                use_cases=[
                    "Asisten AI percakapan real-time dengan empati akustik dan interupsi alami.",
                    "Analisis visual bedah medis dan telemetri video drone secara instan.",
                    "Ingesti menyeluruh repositori jutaan baris kode beserta dokumentasi arsitektur multimedia."
                ],
                risk_and_alignment="Halusinasi visual spasial (spatial misjudgment), deepfake audio cloning; dimitigasi via C2PA Watermarking."
            )
        ]
    ),
    AICategory(
        id="autonomous-agentic",
        numeral="03",
        name="Sistem Agen Otonom & Orkestrasi Multi-Agen",
        english_name="Autonomous Agentic AI & Swarm Orchestration",
        tagline="Agen cerdas berkemampuan tool-use, perbaikan mandiri, computer-use, dan kolaborasi terdesentralisasi.",
        overview=(
            "Agentic AI adalah transisi dari model pasif berbasis teks (statis) menjadi entitas otonom yang memiliki tujuan "
            "(goal-driven), mampu merencanakan strategi berlapis, memanggil API eksternal, memanipulasi GUI desktop "
            "secara visual (Computer Use), dan berkoordinasi dalam kelompok agen (Multi-Agent Swarm)."
        ),
        paradigm_shift="Dari generasi pasif berbasis respons menjadi siklus aksi di lingkungan digital nyata (Act in Environment).",
        items=[
            AITypeItem(
                id="agentic-swarms-computer-use",
                category_id="autonomous-agentic",
                title="Autonomous Multi-Agent & Computer-Use Swarm",
                tagline="Eksekusi tugas digital mandiri melalui antarmuka GUI, terminal, dan protokol MCP.",
                badge="AUTONOMOUS AGENTS",
                description=(
                    "Arsitektur agen berbasis ReAct (Reasoning + Acting) dan Plan-and-Solve yang dilengkapi dengan "
                    "memori episodik/semantik jangka panjang, integrasi Model Context Protocol (MCP), dan kendali sistem operasi langsung."
                ),
                deep_dive=(
                    "Sistem agen canggih saat ini tidak lagi bekerja secara monolitik. Framework seperti LangGraph, CrewAI, "
                    "dan AutoGen membagi tugas besar ke dalam struktur multi-agen khusus: Arsitek, Implementer, Code Reviewer, "
                    "dan Verifier. Dengan kapabilitas 'Computer Use' Anthropic, agen dapat menganalisis layar virtual, menggerakkan pointer mouse, "
                    "mengisi formulir web, serta memvalidasi hasil kerja tanpa campur tangan manusia."
                ),
                key_mechanisms=[
                    "ReAct Loop (Thought -> Action -> Observation -> Reflection) dengan error recovery dinamis.",
                    "Model Context Protocol (MCP) untuk standarisasi interkoneksi tool, database, dan file server.",
                    "Visual GUI Grounding & OS Level Sandboxing (xdotool, accessibility tree parsing).",
                    "Hierarchical & Swarm Multi-Agent Orchestration dengan konsensus terdistribusi."
                ],
                pioneer_models=["Anthropic Claude Computer Use", "OpenAI Swarm Framework", "LangGraph Multi-Agent Engine", "CrewAI Enterprise"],
                architectural_features=[
                    ArchitecturalFeature(
                        title="Siklus Kontrol Otonom ReAct",
                        detail="State transition loop formal agen terhadap lingkungan:",
                        code_or_formula=r"S_{t+1} = \text{Environment}(S_t, A_t), \quad A_t = \pi_\theta(\text{CoT}_t, \mathcal{H}_{t}, \text{Tools})"
                    ),
                    ArchitecturalFeature(
                        title="Protokol Interkoneksi Model Context Protocol (MCP)",
                        detail="Standarisasi RPC JSON-Schema antara LLM Host dan Server Alat Eksternal:",
                        code_or_formula=r'{ "method": "tools/call", "params": { "name": "exec_shell", "arguments": { "cmd": "git commit" } } }'
                    )
                ],
                benchmarks=[
                    BenchmarkMetric(name="SWE-bench Verified (Software Engineering)", score="49.0% - 65.2%", baseline="GPT-4 Classic: 1.8%", description="Penyelesaian isu bug GitHub nyata di repositori open-source tanpa bantuan."),
                    BenchmarkMetric(name="OSWorld (Computer-Use Benchmark)", score="22.0% - 38.5%", baseline="Human Baseline: ~72%", description="Navigasi GUI OS (Ubuntu/Windows) menyelesaikan tugas kantor kompleks."),
                    BenchmarkMetric(name="WebArena (Web Navigation)", score="35.8% - 50.4%", baseline="Scripted Baseline: 12.0%", description="Tugas e-commerce, belanja, administrasi sistem berbasis browser.")
                ],
                computational_complexity="Multi-turn Token Loop (O(K_turns * Context_Size) dengan Memory Compaction)",
                hardware_affinity="Cloud Edge Containerized Sandboxes (Docker/gVisor), Linux Headless Display Server (Xvfb)",
                use_cases=[
                    "Rekayasa perangkat lunak otonom (Full-cycle developer: riset, coding, testing, pull request).",
                    "Operasi DevOps & Incident Response triage 24/7 otomatis.",
                    "Riset intelijen pasar dan konsolidasi data multi-platform otomatis."
                ],
                risk_and_alignment="Risiko Runaway Execution, unauthorized API payments, Prompt Injection; dicegah dengan Human-in-the-Loop gates & sandboxing."
            )
        ]
    ),
    AICategory(
        id="generative-media-world",
        numeral="04",
        name="Model Dunia & Media Generatif Spasial",
        english_name="Generative Media, 3D & World Simulation Models",
        tagline="Sintesis video temporal-konsisten, spatial physics world models, dan audio fotorealistik.",
        overview=(
            "Media generatif telah berevolusi dari sekadar generator gambar 2D statis menjadi Model Dunia (World Models). "
            "Model ini mempelajari representasi spasial 3D implisit, kontinuitas waktu (temporal consistency), serta hukum-hukum "
            "fisika dunia nyata (gravitasi, inersia, fluida, refleksi cahaya) untuk mensimulasikan lingkungan nyata dan virtual."
        ),
        paradigm_shift="Dari estimasi piksel 2D menuju pemahaman simulasi fisika dunia 3D & 4D (Spatial Intelligence).",
        items=[
            AITypeItem(
                id="dit-world-simulator",
                category_id="generative-media-world",
                title="Diffusion Transformers (DiT) & Spatiotemporal World Models",
                tagline="Simulasi fisika dinamis, video fotorealistik 4K, dan aset 3D mesh instan.",
                badge="WORLD MODELS",
                description=(
                    "Arsitektur berbasis Diffusion Transformers (DiT) dan Flow Matching yang beroperasi di dalam ruang laten "
                    "spatiotemporal terkompresi (3D VAE), menghasilkan video definisi tinggi dengan konsistensi objek absolut."
                ),
                deep_dive=(
                    "Sistem seperti OpenAI Sora, Google Veo 2, dan MiniMax Hailuo Video memecah video menjadi 'spatiotemporal patches' "
                    "yang diperlakukan layaknya token bahasa. Model tidak hanya menggambar bingkai gambar, melainkan mempertahankan "
                    "keberadaan objek (object permanence) saat kamera bergerak, berputar 360 derajat, atau saat objek tertutup sementara."
                ),
                key_mechanisms=[
                    "Spatiotemporal Patch Tokenization (3D Latent Patches diproses oleh Transformer Blocks).",
                    "Rectified Flow Matching untuk sampling lebih cepat dan lintasan trajectory yang lurus.",
                    "Spatial Intelligence & Physics Simulation (Kinematika, pencahayaan global, elastisitas).",
                    "Multi-track Neural Audio Synthesis (Suno v4, Udio) dengan pemodelan harmoni polifonik."
                ],
                pioneer_models=["OpenAI Sora", "Google Veo 2", "MiniMax Hailuo Video", "Runway Gen-3 Alpha", "Suno v4 / Udio"],
                architectural_features=[
                    ArchitecturalFeature(
                        title="Rectified Flow Matching ODE",
                        detail="Persamaan diferensial biasa (ODE) untuk memetakan noise Gaussian ke distribusi data video:",
                        code_or_formula=r"\frac{d x_t}{dt} = v_\theta(x_t, t), \quad x_t = t x_1 + (1 - t) x_0"
                    ),
                    ArchitecturalFeature(
                        title="DiT Cross-Attention Spatial Conditioning",
                        detail="Injeksi kondisi teks/kamera ke dalam lapisan Transformer DiT:",
                        code_or_formula=r"h_{l+1} = \text{DiTBlock}(h_l, \text{AdaLN}(y, t))"
                    )
                ],
                benchmarks=[
                    BenchmarkMetric(name="VBench Total Score", score="84.2% - 89.5%", baseline="Early Gen-Video: 58.0%", description="Evaluasi holistik konsistensi subjek, dinamika temporal, dan kualitas visual."),
                    BenchmarkMetric(name="Subject Permanence Score", score="94.1%", baseline="Baseline U-Net: 62.3%", description="Preservasi identitas karakter/benda saat keluar-masuk frame kamera."),
                    BenchmarkMetric(name="Physical Simulation Fidelity", score="81.7%", baseline="Traditional CGI: 95.0%", description="Akurasi pantulan cahaya, dinamika air, dan tumbukan kinetik partikel.")
                ],
                computational_complexity="O(T_frames * H_patches * W_patches * D_model) - Sangat intensif FLOPs",
                hardware_affinity="NVIDIA H100/H200 Multi-Node GPU Clusters dengan NVLink 4.0 dan InfiniBand NDR 400Gbps",
                use_cases=[
                    "Simulasi sintetis training autonomous driving (Waymo, Tesla FSD) untuk edge case langka.",
                    "Produksi sinematografi virtual, CGI otomatis, dan industri kreatif periklanan.",
                    "Generasi lingkungan 3D interaktif untuk simulasi robotika dan game engine (Unreal/Unity)."
                ],
                risk_and_alignment="Disinformasi visual hiper-realistis; ditanggulangi melalui kriptografi metadata C2PA & SynthID watermarking."
            )
        ]
    ),
    AICategory(
        id="architectural-foundations",
        numeral="05",
        name="Fondasi Arsitektural Komputasi AI",
        english_name="Architectural Foundations (Transformers, MoE & SSMs)",
        tagline="Perbandingan struktural antara Dense Transformers, Mixture-of-Experts, dan State Space Models (Mamba).",
        overview=(
            "Di balik kecerdasan buatan modern terdapat fondasi matematika arsitektur model. Pemilihan arsitektur "
            "menentukan rasio efisiensi energi, throughput token per detik, penggunaan VRAM (KV-Cache footprint), "
            "dan skalabilitas jendela konteks dari jutaan hingga miliaran token."
        ),
        paradigm_shift="Diversifikasi arsitektural: dari Dense Transformers murni menuju Sparse MoE dan Linear SSM/Hybrids.",
        items=[
            AITypeItem(
                id="moe-vs-ssm-transformers",
                category_id="architectural-foundations",
                title="Dense vs. Mixture-of-Experts (MoE) vs. State Space Models (Mamba)",
                tagline="Analisis komparatif kompleksitas waktu dan efisiensi memori arsitektur saraf tiruan terkini.",
                badge="CORE ARCHITECTURE",
                description=(
                    "Komparasi mendalam antara Dense Attention ($O(N^2)$), Sparse Mixture-of-Experts (MoE) dengan "
                    "routing dinamis, dan State Space Models ($O(N)$) seperti Mamba 2 dan Recurrent Griffin."
                ),
                deep_dive=(
                    "1. **Dense Transformers**: Mengaktifkan 100% parameter pada setiap token. Sangat stabil dalam pre-training, namun biaya komputasi membengkak secara kuadratik seiring panjangnya konteks.\n"
                    "2. **Mixture-of-Experts (MoE)**: Menggantikan lapisan Feed-Forward Network (FFN) dengan puluhan/ratusan 'ahli' (experts). Router pintar (Top-k gating) hanya mengaktifkan subset kecil (misal: 8 dari 128 experts, seperti pada DeepSeek-V3), memangkas biaya FLOPs hingga 70% sambil mempertahankan kapasitas parameter total yang masif.\n"
                    "3. **State Space Models (SSM/Mamba & Hybrid Recurrent)**: Menggunakan formulasi waktu-kontinu yang didiskritisasi menjadi matriks status linier. Meniadakan KV-Cache kuadratik, menghasilkan decoding berkecepatan konstan $O(1)$ untuk streaming teks tak terbatas."
                ),
                key_mechanisms=[
                    "Dense Self-Attention: $O(N^2)$ kompleksitas waktu, kebutuhan memori KV-Cache linier per layer.",
                    "Sparse MoE Gating: Top-K Softmax Routing dengan Auxiliary Loss untuk load balancing antar expert.",
                    "Mamba SSM Selective Scan: Time-Varying Linear Differential Equations dengan Hardware-Aware Parallel Scan (Flash-Scan).",
                    "Hybrid Architectures (e.g. Jamba, Griffin): Menggabungkan atensi lokal dengan blok SSM linier global."
                ],
                pioneer_models=["DeepSeek-V3 / R1 (MoE 671B/37B active)", "Mixtral 8x22B", "Mamba 2 (State Space Model)", "AI21 Jamba 1.5 Hybrid"],
                architectural_features=[
                    ArchitecturalFeature(
                        title="Top-K MoE Routing Formulation",
                        detail="Probabilitas pemilihan expert untuk token x:",
                        code_or_formula=r"G(x) = \text{Softmax}(\text{TopK}(H(x), k)), \quad y = \sum_{i=1}^{k} G(x)_i \cdot E_i(x)"
                    ),
                    ArchitecturalFeature(
                        title="Selective State Space Model (SSM Discretization)",
                        detail="Evolusi state h(t) dalam sistem Mamba linier:",
                        code_or_formula=r"h_t = \bar{A} h_{t-1} + \bar{B} x_t, \quad y_t = C_t h_t + D x_t"
                    )
                ],
                benchmarks=[
                    BenchmarkMetric(name="Decoding Throughput (Tokens/Sec)", score="SSM: 3.5x faster, MoE: 2.2x faster", baseline="Dense Transformer: 1.0x baseline", description="Kecepatan generasi token pada konteks panjang 128k token."),
                    BenchmarkMetric(name="KV-Cache VRAM Allocation", score="Mamba: ~0.1 GB (Constant), MoE: 8-16 GB", baseline="Dense Attention: 38+ GB", description="Konsumsi memori VRAM GPU untuk menyimpan cache konteks."),
                    BenchmarkMetric(name="Pre-training Compute Efficiency", score="MoE: 3.8x FLOPs efficiency", baseline="Dense Baseline: 1.0x", description="Kualitas model per satuan energi kilowatt-hour.")
                ],
                computational_complexity="Dense: O(N^2), MoE: O(N * K_active_experts), SSM/Mamba: O(N)",
                hardware_affinity="SRAM Kernel Fusion (Triton/CUDA), High Bandwidth Interconnect (NVSwitch) untuk MoE All-to-All communication",
                use_cases=[
                    "Infrastruktur Cloud Serving berskala jutaan pengguna bersamaan dengan biaya operasional minimal.",
                    "Edge Device & On-Device AI (smartphone, robotika, IoT) yang memiliki limitasi daya baterai dan memori.",
                    "Pemrosesan aliran data waktu nyata (financial high-frequency trading, IoT sensor streams)."
                ],
                risk_and_alignment="Expert Routing Collapse (beberapa expert tidak terpakai), SSM recall degradation pada associative retrieval kompleks."
            )
        ]
    ),
    AICategory(
        id="narrow-ai-to-agi",
        numeral="06",
        name="Narrow AI (ANI) menuju Peta Jalan AGI & Penyelarasan",
        english_name="Narrow AI to AGI Roadmap & AI Alignment",
        tagline="Transisi kecerdasan spesifik menuju kecerdasan umum buatan dan kerangka keamanan etis.",
        overview=(
            "Kecerdasan Buatan bergerak dari Narrow AI (sistem spesifik seperti AlphaFold atau filter spam) "
            "menuju Artificial General Intelligence (AGI) yang memiliki fleksibilitas kognitif setara atau melampaui "
            "manusia terdidik di hampir seluruh bidang ekonomi berharga. Perjalanan ini mewajibkan protokol keselamatan ketat (AI Safety)."
        ),
        paradigm_shift="Evolusi dari algoritma terisolasi (Narrow) menuju sistem kognisi universal adaptif (AGI).",
        items=[
            AITypeItem(
                id="agi-levels-alignment",
                category_id="narrow-ai-to-agi",
                title="Peta Jalan 5 Tingkat AGI & Kerangka AI Alignment",
                tagline="Taksonomi kematangan kognitif dan sistem penjajaran nilai kemanusiaan (Constitutional AI).",
                badge="AGI ROADMAP & SAFETY",
                description=(
                    "Kerangka taksonomi 5 tingkat AGI (DeepMind/OpenAI standard) yang mengukur otonomi, generalitas, "
                    "dan ketahanan sistem terhadap skenario kegagalan, dilengkapi protokol keamanan AI Alignment."
                ),
                deep_dive=(
                    "Tingkat Kematangan AGI:\n"
                    "- **Level 0 (No AI)**: Perangkat lunak kalkulator dan database deterministik.\n"
                    "- **Level 1 (Emerging)**: Chatbot dasar tanpa penalaran mandiri (misal: ChatGPT generasi awal).\n"
                    "- **Level 2 (Competent)**: Model penalaran setara 50% manusia dewasa terampil (o1, DeepSeek-R1).\n"
                    "- **Level 3 (Expert)**: Model setara 90% profesional terampil (Autonomous Software Engineers, Copilot swarms).\n"
                    "- **Level 4 (Virtuoso)**: Model setara 99% manusia terbaik di bidangnya (sintesis riset ilmiah baru, AlphaFold 3).\n"
                    "- **Level 5 (Superhuman / ASI)**: Melampaui kapasitas seluruh umat manusia secara kolektif.\n\n"
                    "**Pilar Keselamatan (AI Alignment)**:\n"
                    "1. *Constitutional AI (RLAIF)*: Model mengkritisi dan mengoreksi diri berdasarkan prinsip konstitusi etika tertulis.\n"
                    "2. *Mechanistic Interpretability*: Mengurai representasi 'black-box' sirkuit saraf buatan untuk mendeteksi penipuan internal (deception).\n"
                    "3. *Sandboxed Deployment*: Menjalankan kode agen di lingkungan virtual terisolasi tanpa akses jaringan luar tanpa otorisasi."
                ),
                key_mechanisms=[
                    "5-Tier AGI Capability Ladder (Emerging -> Competent -> Expert -> Virtuoso -> Superhuman).",
                    "Constitutional AI & Reinforcement Learning from AI Feedback (RLAIF).",
                    "Mechanistic Interpretability & Sparse Autoencoders (SAE) untuk feature extraction pada aktivasi residu.",
                    "Scalable Oversight & Debate Protocols untuk verifikasi sistem yang lebih pintar dari pengawas manusia."
                ],
                pioneer_models=["Google DeepMind AlphaFold 3", "Anthropic Constitutional Claude", "OpenAI Alignment Evals Suite"],
                architectural_features=[
                    ArchitecturalFeature(
                        title="Sparse Autoencoders (SAE) untuk Interpretasi Fitur",
                        detail="Dekomposisi aktivasi tersembunyi menjadi fitur monosemantik yang dapat dipahami manusia:",
                        code_or_formula=r"x \approx \sum_{i=1}^{M} f_i(x) \cdot d_i, \quad f_i(x) = \text{ReLU}(W_{enc} x + b_{enc})"
                    ),
                    ArchitecturalFeature(
                        title="Loss Penjajaran Konstitusional (RLAIF Loss)",
                        detail="Optimalisasi kebijakan berbasis preferensi konstitusi etis:",
                        code_or_formula=r"\mathcal{L}_{\text{RLAIF}} = -\mathbb{E}_{(x, y_w, y_l)} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w|x)}{\pi_{\text{ref}}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{\text{ref}}(y_l|x)} \right) \right]"
                    )
                ],
                benchmarks=[
                    BenchmarkMetric(name="ARC-AGI (Abstraction & Reasoning Corpus)", score="53.6% - 75.7%", baseline="Average Human: 85.0%", description="Uji kemampuan penalaran abstrak pada teka-teki logika yang belum pernah dilihat dalam data latihan."),
                    BenchmarkMetric(name="MMLU-Pro (Reasoning Benchmark)", score="72.6% - 84.0%", baseline="Human College Expert: 70.0%", description="Evaluasi penalaran multi-bidang dengan pilihan distraktor tingkat lanjut."),
                    BenchmarkMetric(name="Refusal & Safety Alignment Rate", score="99.4% Robustness", baseline="Uncensored Base: 40.0%", description="Ketahanan terhadap serangan adversarial jailbreak dan permintaan berbahaya (CBRN).")
                ],
                computational_complexity="Eksponensial frontier compute scaling + Continuous safety audit overhead",
                hardware_affinity="Sovereign AI Compute Clusters, Multi-Datacenter Distributed Training Pods",
                use_cases=[
                    "Penemuan material superkonduktor suhu kamar dan fusi nuklir terkendali.",
                    "Otomatisasi riset sains dan penulisan paper ilmiah otonom.",
                    "Sistem tata kelola makroekonomi dan alokasi sumber daya global optimal."
                ],
                risk_and_alignment="Eksistensial Risk (x-risk), Autonomous Weaponry, Power-Seeking Behavior; diatur via Trajectory Auditing & Red-Teaming."
            )
        ]
    )
]
