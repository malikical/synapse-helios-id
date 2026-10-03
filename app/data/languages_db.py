"""
SYNAPSE HELIOS ID - AI Programming Languages & Software Engineering Database
Arsitektur Bahasa Komputasi AI & Rekayasa Perangkat Lunak Modern
"""
from typing import List
from app.models.programming_lang import ProgrammingLanguage

AI_LANGUAGES_DATA: List[ProgrammingLanguage] = [
    ProgrammingLanguage(
        id="python",
        name="Python",
        version_standard="3.12+ / 3.13 (Free-Threaded GIL)",
        logo_url="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg",
        role_indonesian="Tulang Punggung Ekosistem AI, Deep Learning, & Orkestrasi Agen",
        primary_ecosystem="PyTorch, TensorFlow, Hugging Face Transformers, LangChain, AutoGen, vLLM Python SDK",
        performance_tier="Level 3 - High-Level Orchestration / C-Binding Engine",
        specific_use_cases=[
            "Pelatihan (training) model saraf tiruan deep learning berskala besar.",
            "Riset model matematika dan prototipe arsitektur kognitif baru.",
            "Orkestrasi multi-agen otonom dan eksekusi skrip komputasi ilmiah."
        ],
        architectural_role=(
            "Python bertindak sebagai 'lingua franca' kecerdasan buatan global. Meskipun berjalan sebagai bahasa ber-interpreter, "
            "Python berfungsi sebagai lapisan kendali tingkat tinggi (control plane) elegan yang membungkus kernel C++/CUDA di lapisan bawah, "
            "memberikan produktivitas pengembang tak tertandingi."
        ),
        strengths=[
            "Ekosistem pustaka AI/ML terlengkap di dunia (ribuan modul mutakhir).",
            "Sintaks intuitif dan ekspresif untuk manipulasi tensor dan aljabar linier.",
            "Dukungan interoperabilitas native dengan C/C++, Rust, dan akselerator GPU."
        ],
        code_example_title="PyTorch Neural Tensor Flow with Attention",
        code_example="""import torch
import torch.nn as nn

class MultiHeadAttentionBlock(nn.Module):
    def __init__(self, d_model: int = 512, n_heads: int = 8):
        super().__init__()
        self.d_model = d_model
        self.n_heads = n_heads
        self.head_dim = d_model // n_heads
        self.q_proj = nn.Linear(d_model, d_model, bias=False)
        self.k_proj = nn.Linear(d_model, d_model, bias=False)
        self.v_proj = nn.Linear(d_model, d_model, bias=False)
        self.out_proj = nn.Linear(d_model, d_model, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        batch_size, seq_len, _ = x.shape
        # Proyeksi linier terfusi
        q = self.q_proj(x).view(batch_size, seq_len, self.n_heads, self.head_dim).transpose(1, 2)
        k = self.k_proj(x).view(batch_size, seq_len, self.n_heads, self.head_dim).transpose(1, 2)
        v = self.v_proj(x).view(batch_size, seq_len, self.n_heads, self.head_dim).transpose(1, 2)
        
        # FlashAttention Kernel Execution
        out = torch.nn.functional.scaled_dot_product_attention(q, k, v, is_causal=True)
        out = out.transpose(1, 2).contiguous().view(batch_size, seq_len, self.d_model)
        return self.out_proj(out)""",
        runtime_environment="CPython 3.12+, PyPy, uv, TorchScript, Triton JIT",
        metrics={
            "Adopsi Ekosistem": "99.2%",
            "Efisiensi Developer": "98.5%",
            "Performa Native": "62.0% (Tergantung C-Backend)",
            "Kapasitas Konkurensi": "78.0% (PEP 703 No-GIL)"
        }
    ),
    ProgrammingLanguage(
        id="typescript-javascript",
        name="TypeScript / JavaScript",
        version_standard="TypeScript 5.6+ / ES2024 (Node.js & V8)",
        logo_url="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg",
        role_indonesian="Frontend AI UI/UX, Edge Agent Runtime, & Cloudflare Workers",
        primary_ecosystem="Vercel AI SDK, LangChain.js, ONNX Runtime Web, Cloudflare Workers AI, Transformers.js",
        performance_tier="Level 3 - High-Throughput Asynchronous Edge I/O",
        specific_use_cases=[
            "Antarmuka pengguna interaktif real-time dengan streaming SSE token AI.",
            "Eksekusi pipeline agen terdistribusi di Edge serverless tanpa cold start.",
            "Inference on-device langsung di browser web menggunakan WebGPU dan WASM."
        ],
        architectural_role=(
            "TypeScript menghubungkan kecerdasan buatan backend langsung ke sentuhan pengguna akhir. "
            "Melalui Vercel AI SDK dan ekosistem edge serverless, TypeScript memimpin arsitektur antarmuka streaming, "
            "generative UI, dan orkestrasi tool-calling yang aman tipe (strictly typed schema validation)."
        ),
        strengths=[
            "Sistem tipe statis kuat dengan JSON-Schema inference otomatis (Zod).",
            "Event-loop asinkron non-blocking yang sangat efisien untuk jutaan koneksi streaming I/O.",
            "Kemampuan eksekusi model on-device di browser via WebGPU (zero server cost)."
        ],
        code_example_title="Edge Agent Streaming Inference with Tool Calling",
        code_example="""import { generateText, tool } from 'ai';
import { z } from 'zod';

export async function executeAgentWorkflow(userPrompt: string) {
  const result = await generateText({
    model: 'synapse-gemini-3-flash',
    prompt: userPrompt,
    tools: {
      queryDatabase: tool({
        description: 'Ambil metrik kognisi dari klaster AI Indonesia',
        parameters: z.object({
          clusterId: z.string(),
          metricType: z.enum(['latency', 'throughput', 'vram']),
        }),
        execute: async ({ clusterId, metricType }) => {
          return { status: 'ONLINE', clusterId, value: '0.04ms' };
        },
      }),
    },
  });

  return result;
}""",
        runtime_environment="Node.js 20+, Bun 1.1+, Deno 2.0, Cloudflare Workers V8",
        metrics={
            "Adopsi Ekosistem": "94.5%",
            "Efisiensi Developer": "96.0%",
            "Performa Native": "84.0% (V8 JIT / WebGPU)",
            "Kapasitas Konkurensi": "97.5% (Async Event Loop)"
        }
    ),
    ProgrammingLanguage(
        id="cplusplus-cuda",
        name="C++ / CUDA",
        version_standard="C++20 / C++23, CUDA 12.6+ / PTX ISA",
        logo_url="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg",
        role_indonesian="Akselerasi Komputasi GPU Rendah, Kernel Optimization, & Engine Inferensi (vLLM, llama.cpp)",
        primary_ecosystem="NVIDIA CUDA Toolkit, TensorRT-LLM, llama.cpp, vLLM Kernels, CUTLASS, FlashAttention C++",
        performance_tier="Level 1 - Ultra Bare Metal / Hardware Native",
        specific_use_cases=[
            "Penulisan kernel kustom GPU (custom CUDA kernels) untuk operasi tensor baru.",
            "Engine inferensi performa ekstrem berlatensi mikrodetik (vLLM, TensorRT).",
            "Kuantisasi bobot model (INT4, FP8, AWQ, GGUF) dan optimasi memory bandwidth."
        ],
        architectural_role=(
            "C++ dan CUDA adalah fondasi absolut di mana seluruh komputasi kecerdasan buatan dijalankan. "
            "Setiap operasi matriks perkalian (GEMM), attention block, dan transfer tensor antar GPU NVLink "
            "didesain menggunakan C++ dan instruksi CUDA tingkat rendah untuk memaksimalkan throughput FLOPS chip silikon."
        ),
        strengths=[
            "Kendali memori fisik dan registri GPU secara manual tanpa overhead.",
            "Pemanfaatan penuh Tensor Cores dan memori shared memory (SRAM) GPU.",
            "Kecepatan komputasi maksimum mendekati limit teoritis perangkat keras."
        ],
        code_example_title="Custom CUDA Kernel for Fast Fused Softmax",
        code_example="""#include <cuda_runtime.h>
#include <device_launch_parameters.h>

__global__ void FusedOnlineSoftmaxKernel(
    const float* __restrict__ input,
    float* __restrict__ output,
    int batch_size,
    int seq_len
) {
    int row = blockIdx.x * blockDim.x + threadIdx.x;
    if (row >= batch_size) return;

    const float* row_in = input + row * seq_len;
    float* row_out = output + row * seq_len;

    float max_val = -1e20f;
    #pragma unroll
    for (int i = 0; i < seq_len; ++i) {
        max_val = fmaxf(max_val, row_in[i]);
    }

    float sum_exp = 0.0f;
    #pragma unroll
    for (int i = 0; i < seq_len; ++i) {
        float exp_v = __expf(row_in[i] - max_val);
        row_out[i] = exp_v;
        sum_exp += exp_v;
    }

    float inv_sum = 1.0f / sum_exp;
    #pragma unroll
    for (int i = 0; i < seq_len; ++i) {
        row_out[i] *= inv_sum;
    }
}""",
        runtime_environment="NVIDIA NVCC, Clang/LLVM, GCC 14, Host Linux Driver Kernel",
        metrics={
            "Adopsi Ekosistem": "96.0%",
            "Efisiensi Developer": "55.0% (Kompleksitas Tinggi)",
            "Performa Native": "100.0% (Hardware Limit)",
            "Kapasitas Konkurensi": "99.9% (Massive GPU Warps)"
        }
    ),
    ProgrammingLanguage(
        id="rust",
        name="Rust",
        version_standard="Rust Edition 2021 / 2024 (1.82+)",
        logo_url="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-original.svg",
        role_indonesian="High-Performance Memory-Safe Serving Engines (Candle, Burn, Tokenizers)",
        primary_ecosystem="Hugging Face Candle, Burn Framework, tokenizers (Rust crate), Mistral.rs, Polars",
        performance_tier="Level 1 - Zero-Cost Abstraction & Memory Safety",
        specific_use_cases=[
            "Serving engine inferensi berkecepatan setara C++ tanpa risiko memory leak atau segfault.",
            "Tokenisasi teks berkecepatan gigabyte per detik (Hugging Face tokenizers).",
            "Aplikasi AI embedded dan edge runtime yang membutuhkan keandalan crash-free 100%."
        ],
        architectural_role=(
            "Rust merevolusi infrastruktur sistem AI dengan menghadirkan performa setara C/C++ "
            "namun dengan jaminan keamanan memori (memory safety) tanpa garbage collector. "
            "Rust menjadi pilihan utama untuk microservices inferensi kritis, server tokenisasi berkecepatan tinggi, dan runtime on-device."
        ),
        strengths=[
            "Sistem kepemilikan (Ownership & Borrow Checker) mencegah data race pada thread konkuren.",
            "Zero-cost abstraction dengan efisiensi konsumsi CPU dan RAM minimal.",
            "Ekosistem crate modern (Cargo) yang sangat ergonomis dan terintegrasi aman."
        ],
        code_example_title="Rust Candle Native Tensor Matrix Multiplication",
        code_example="""use candle_core::{Device, Result, Tensor};

fn compute_synapse_attention(seq_len: usize, d_model: usize) -> Result<Tensor> {
    let device = Device::cuda_if_available(0).unwrap_or(Device::Cpu);
    
    // Inisialisasi tensor bobot
    let q = Tensor::randn(0f32, 1.0, (1, seq_len, d_model), &device)?;
    let k = Tensor::randn(0f32, 1.0, (1, seq_len, d_model), &device)?;
    
    // Transpose matriks kunci (K)
    let k_t = k.transpose(1, 2)?;
    
    // Perkalian tensor terakselerasi aman (Q @ K^T)
    let scores = q.matmul(&k_t)?;
    let scaled_scores = (scores / (d_model as f64).sqrt())?;
    
    // Softmax aman
    let attention_weights = candle_nn::ops::softmax(&scaled_scores, 2)?;
    Ok(attention_weights)
}""",
        runtime_environment="Rustc / LLVM, Cargo, WASM Target, CUDA/Metal Bindings",
        metrics={
            "Adopsi Ekosistem": "82.0%",
            "Efisiensi Developer": "78.0%",
            "Performa Native": "99.0% (Zero Overhead)",
            "Kapasitas Konkurensi": "100.0% (Fearless Concurrency)"
        }
    ),
    ProgrammingLanguage(
        id="mojo",
        name="Mojo",
        version_standard="Mojo 24.5+ (Modular MAX Platform)",
        logo_url="https://raw.githubusercontent.com/modularml/mojo/main/assets/images/mojo-logo.png",
        role_indonesian="Bahasa Generasi Baru untuk Akselerator AI (Sintaks Python + Kecepatan C++)",
        primary_ecosystem="Modular MAX Engine, Mojo Standard Library, MAX Graph Compiler, Python Interop",
        performance_tier="Level 1 - Hardware Programmable Accelerator Native",
        specific_use_cases=[
            "Pemrograman akselerator AI (GPU, CPU AVX-512/AMX, NPU) dengan sintaks semudah Python.",
            "Pengganti custom C++/CUDA kernel dengan portabilitas lintas vendor hardware (NVIDIA, AMD, Intel).",
            "Kompilasi graf model AI langsung ke binary tanpa dependensi runtime Python berat."
        ],
        architectural_role=(
            "Mojo dirancang khusus oleh pencipta LLVM & Swift (Chris Lattner) untuk memecahkan 'masalah dua bahasa' "
            "(two-language problem) dalam AI. Mojo memberikan fleksibilitas sintaks Python namun dapat dikompilasi "
            "langsung ke instruksi SIMD hardware dengan kecepatan hingga 68.000x lebih cepat dibanding Python standar."
        ),
        strengths=[
            "Kompatibilitas penuh dengan sintaks dan pustaka Python (NumPy, PyTorch) secara instan.",
            "Dukungan native untuk autotuning, parameterisasi metaprogramming, dan SIMD vectorization.",
            "Model kepemilikan memori eksplisit (let, var, fn, struct) untuk efisiensi perangkat keras ekstrem."
        ],
        code_example_title="Mojo SIMD Vectorized Tensor Parallelism",
        code_example="""from algorithm import parallelize, vectorize
from sys.info import simdwidthof

alias type = DType.float32
alias simd_width = simdwidthof[type]()

fn fused_matrix_add[size: Int](inout a: DTypePointer[type], b: DTypePointer[type]):
    @parameter
    fn compute_vector[width: Int](idx: Int):
        let v_a = a.load[width=width](idx)
        let v_b = b.load[width=width](idx)
        a.store[width=width](idx, v_a + v_b)

    vectorize[compute_vector, simd_width](size)

fn main():
    print("Mojo Synapse Neural Kernel Initialized.")""",
        runtime_environment="Modular Mojo Compiler, MLIR (Multi-Level Intermediate Representation), LLVM",
        metrics={
            "Adopsi Ekosistem": "68.0% (Pertumbuhan Sangat Cepat)",
            "Efisiensi Developer": "92.0%",
            "Performa Native": "99.5% (SIMD Autotuned)",
            "Kapasitas Konkurensi": "98.0% (Hardware Vector Native)"
        }
    ),
    ProgrammingLanguage(
        id="golang",
        name="Go (Golang)",
        version_standard="Go 1.23+ / 1.24",
        logo_url="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original-wordmark.svg",
        role_indonesian="Orkestrasi Microservices AI, Distributed Gateways, & Kubernetes Operators",
        primary_ecosystem="Ollama (Core Engine), Kubernetes AI Operators, KServe, LocalAI, Fiber, gRPC",
        performance_tier="Level 2 - High Concurrency Distributed Service Mesh",
        specific_use_cases=[
            "Gateway inferensi terdistribusi dan load balancer cerdas untuk klaster GPU.",
            "Aplikasi runner model lokal seperti Ollama yang mengorkestrasi inferensi biner.",
            "Kubernetes CRD controllers dan pipeline orkestrasi data stream bervolume masif."
        ],
        architectural_role=(
            "Go adalah tulang punggung infrastruktur cloud-native AI. Sementara komputasi tensor berat "
            "berjalan di GPU, Go mengendalikan ribuan goroutine ringan untuk menangani traffic API, antrean inferensi, "
            "sinkronisasi status klaster, dan autoscaling serverless pod GPU secara deterministik."
        ),
        strengths=[
            "Goroutine ringan (overhead hanya ~2KB memori) yang mampu menangani ratusan ribu koneksi simultan.",
            "Kompilasi single-binary tanpa dependensi dinamis yang mempermudah deployment Docker.",
            "Waktu kompilasi ultra-cepat dan sistem perkabelan jaringan I/O (gRPC/HTTP3) kelas enterprise."
        ],
        code_example_title="Go Concurrent AI Inference Gateway with Goroutines",
        code_example="""package main

import (
	"context"
	"fmt"
	"net/http"
	"sync"
	"time"
)

type InferenceGateway struct {
	mu       sync.RWMutex
	nodePool []string
}

func (g *InferenceGateway) DispatchStream(ctx context.Context, prompt string) (<-chan string, error) {
	out := make(chan string, 100)
	go func() {
		defer close(out)
		// Streaming token generator concurrently
		for i := 0; i < 5; i++ {
			select {
			case <-ctx.Done():
				return
			case out <- fmt.Sprintf("[CHUNK_%d: Neural tensor active]", i):
				time.Sleep(15 * time.Millisecond)
			}
		}
	}()
	return out, nil
}""",
        runtime_environment="Go Runtime, GC Concurrent Tri-color, Linux amd64/arm64",
        metrics={
            "Adopsi Ekosistem": "90.0%",
            "Efisiensi Developer": "93.0%",
            "Performa Native": "90.0% (Compiled Native)",
            "Kapasitas Konkurensi": "100.0% (Goroutine Scaling)"
        }
    ),
    ProgrammingLanguage(
        id="julia",
        name="Julia",
        version_standard="Julia 1.10 LTS / 1.11",
        logo_url="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/julia/julia-original.svg",
        role_indonesian="Riset Saintifik Numerik Tinggi, Diferensiasi Otomatis, & Pemodelan Fisika",
        primary_ecosystem="Flux.jl, Lux.jl, DifferentialEquations.jl, CUDA.jl, Zygote.jl, Scientific ML (SciML)",
        performance_tier="Level 1 - High-Level Multiple Dispatch / JIT Native",
        specific_use_cases=[
            "Scientific Machine Learning (SciML) yang menggabungkan model fisika diferensial dengan neural network.",
            "Diferensiasi otomatis menyeluruh pada simulasi dinamika fluida dan iklim global.",
            "Pemodelan sistem kuantum dan kalkulasi tensor dimensi tinggi tanpa konversi bahasa."
        ],
        architectural_role=(
            "Julia memadukan kemudahan matematika linear layaknya MATLAB/Python dengan kecepatan komputasi C. "
            "Melalui paradigma *Multiple Dispatch*, Julia memungkinkan seluruh algoritma machine learning dan "
            "persamaan diferensial ditulis 100% dalam Julia murni tanpa memerlukan lapisan ekstensi C/C++ eksternal."
        ),
        strengths=[
            "Multiple Dispatch memungkinkan komposabilitas kode tingkat tinggi yang belum pernah ada sebelumnya.",
            "Diferensiasi otomatis (Automatic Differentiation) native hingga ke level kontrol flow bahasa.",
            "Kompilasi LLVM JIT yang menghasilkan instruksi mesin biner berkecepatan setara C/Fortran."
        ],
        code_example_title="Julia Scientific Neural Differential Equation (SciML)",
        code_example="""using DifferentialEquations, Lux, ComponentArrays, Random

# Definisi Neural ODE untuk pemodelan fisika kontinu
struct NeuralODE{M}
    model::M
end

function (node::NeuralODE)(u, p, t)
    # Evaluasi gradien tensor kontinu dalam ruang laten
    return node.model(u, p.model, p.state)[1]
end

# Inisialisasi solver diferensial waktu-nyata
rng = Random.default_rng()
nn_layer = Lux.Chain(Lux.Dense(2 => 16, tanh), Lux.Dense(16 => 2))
p, st = Lux.setup(rng, nn_layer)

println("Julia SciML Synapse Core Ready.")""",
        runtime_environment="Julia LLVM JIT, OpenBLAS, CUDA.jl Native Kernels",
        metrics={
            "Adopsi Ekosistem": "74.0%",
            "Efisiensi Developer": "89.0%",
            "Performa Native": "98.0% (LLVM JIT Compiled)",
            "Kapasitas Konkurensi": "86.0% (Multi-threaded Tasks)"
        }
    )
]
