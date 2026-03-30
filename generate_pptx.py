from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

# Slide definitions
slides_data = [
    {
        "title": "The Architecture of AI Progress: Synthesizing the Formal Foundations and Empirical Drivers of Artificial Intelligence",
        "bullets": [
            "A Unified Theoretical Framework: Presenting a cohesive research program that bridges theoretical limits and engineering realities",
            "Two Connected Pairs:",
            "  Pair 1 (The Formal Foundation): Intelligence defined by its outer boundary of computability and inner boundary of polynomial-time feasibility",
            "  Pair 2 (The Practical Bridge): The empirical driver of scaling laws and the architectural consequences of hardware allocation"
        ]
    },
    {
        "title": "The Discourse Gap: Why This Program Exists",
        "bullets": [
            "The Hype: Empirical AI discourse often focuses on capability scaling and scaling laws without a rigorous formal theory of progress",
            "The Limits: Theoretical discourse frequently emphasizes strict mathematical limits without explaining how relentless practical progress continues to appear",
            "The Missing Link: We require a single, unified model that explains how formal boundaries, empirical drivers, and system-level architectural consequences interact"
        ]
    },
    {
        "title": "The Two-Pair Structure of AI Progress",
        "bullets": [
            "Pair 1: The Formal Foundation",
            "  Paper 1 (Computability): Intelligence as an open-ended limiting process at the outer boundary of what can be mechanized",
            "  Paper 2 (Complexity): Intelligence as a staged bounded ascent at the inner boundary of polynomial-time reachability",
            "Pair 2: The Empirical and Architectural Bridge",
            "  Paper 3 (Scaling Laws): How abstract scaling drives progress and enforces a race for hidden efficiency",
            "  Paper 4 (Modernized Amdahl): How the pressure of scaling reshapes the hardware allocation between specialized and programmable compute"
        ]
    },
    {
        "title": "Paper 1: The Computability Boundary",
        "bullets": [
            "Beyond a Fixed Closure: Intelligence is not one finitely specifiable, fixed rule-governed procedure",
            "The Limiting-Process Structure: When a process is mechanized, the higher-order task of guiding, specifying, and evaluating that mechanization is displaced upward to a new level",
            "Local Mechanization vs. Open Boundary: Every established, mechanized computational layer possesses a canonical, relatively uncomputable open boundary"
        ]
    },
    {
        "title": "Paper 1: The Mechanics of Ascent",
        "bullets": [
            "[Visual Concept: A blueprint-style diagram showing a foundational layer A_n, ascending through an intermediate step, toward an open ceiling A'_n]",
            "The Turing Jump as a Ceiling: The absolute boundary of any mechanized layer is its Turing jump (A')",
            "Progressive Layers: Real progress occurs through intermediate strengthenings (A <_T B <_T A'), mechanizing steps strictly below the absolute jump",
            "Non-Capture: No single settled layer captures the entire open-ended process of intelligence"
        ]
    },
    {
        "title": "Paper 2: The Feasibility Boundary",
        "bullets": [
            "Redefining Feasibility: The practical reach of intelligence is not a binary “P = NP or nothing” scenario",
            "Expanding Reachability: Progress manifests as progressively wider polynomial-time reach across difficult search tasks",
            "Staged Bounded Ascent: Moving upward by internalizing richer structures of guided search while remaining feasible under strict polynomial-time constraints"
        ]
    },
    {
        "title": "Paper 2: The Polynomial Hierarchy as Limiting Process",
        "bullets": [
            "[Visual Concept: A finite-depth ladder expanding upward, showing P→NP→PH]",
            "Bounded Verification Games: The Polynomial Hierarchy provides a finite-depth ladder of structured proposal, challenge, and repair",
            "Internalizing Search: Moving up the hierarchy allows a system to absorb what was previously external search into a stronger—but still explicitly bounded—verification framework"
        ]
    },
    {
        "title": "Synthesis of Pair 1: The Map of Formal Boundaries",
        "bullets": [
            "[Visual Concept: A nested boundary map showing Well-defined tasks → Computable tasks → Polynomial-time tasks]",
            "The Outer Boundary (Computability): The divide between computable tasks and uncomputable, open-ended well-defined tasks",
            "The Inner Boundary (Feasibility): The divide between what is merely computable in principle and what is polynomial-time reachable in practice"
        ]
    },
    {
        "title": "The Empirical Gap: Why Pair 1 is Not Enough",
        "bullets": [
            "The Transition: Pair 1 provides the formal structure, explaining exactly what progress means mathematically",
            "The Missing Engine: Formal limits alone do not explain why progress continually appears in real-world systems",
            "We must bridge the gap between formal structure and empirical hardware realities"
        ]
    },
    {
        "title": "Paper 3: Scaling Laws and Logical Compute",
        "bullets": [
            "The Power of Abstraction: Scaling laws are unreasonably effective precisely because they abstract over realization details",
            "Logical vs. Physical Compute: The \"compute\" variable actually represents logical compute (abstract model-side work), independent of the efficiency of the physical hardware",
            "The Real Meaning of Diminishing Returns: A flattening scaling curve does not just mean slower progress; it represents a rapidly escalating physical and operational burden to achieve the next step of value"
        ]
    },
    {
        "title": "Paper 3: The Dynamic Implication of Hidden Efficiency",
        "bullets": [
            "[Visual Concept: A pressure-conversion loop showing logical compute demand driving efficiency optimization across the stack]",
            "The Efficiency Race: Progress persists because of repeated, compounding efficiency gains in algorithms, low-precision software, systems, and hardware",
            "Changing the Cost: The empirical scaling law dictates what logical compute buys; the compounding efficiency stack constantly changes what that compute costs"
        ]
    },
    {
        "title": "Paper 4: Modernizing Amdahl’s Law",
        "bullets": [
            "Beyond Core Counts: Classical Amdahl’s Law (fixed serial/parallel fraction) fails to describe modern heterogeneous AI architectures",
            "Constrained Hardware Allocation: The modern design question is how to allocate a constrained hardware budget between specialized logic and programmable compute",
            "The Value-Scalable Fraction (S): The portion of the workload where injecting additional compute continues to create meaningful, end-to-end task value"
        ]
    },
    {
        "title": "Paper 4: The Collapse Threshold of Specialization",
        "bullets": [
            "[Visual Concept: A phase-boundary graph showing the race between Specialization Efficiency (R) and Scalable Fraction (S)]",
            "The Rising Bar: As the value-scalable workload (S) grows, fixed-function specialization faces a strict collapse threshold",
            "The Key Equation: For a given scalable fraction S, specialized hardware must achieve a relative efficiency ratio of R_c = 1/(1−S) to justify its inclusion",
            "Specialization must constantly re-earn its silicon"
        ]
    },
    {
        "title": "Architectural Consequence: The Pressure for Programmability",
        "bullets": [
            "Shifting Value: AI scaling pushes value-generation away from early fixed pipelines toward learned, late-stage computation (e.g., neural reconstruction, massive rerankers)",
            "Why GPUs Become More Programmable: As S rises, the optimal hardware locus shifts toward generalized, tensor-heavy programmable compute",
            "The Accelerator Dynamic: AI domain-specific accelerators matter, but they do not simply displace the GPU; they must continually adapt as the dominant value-producing workload evolves"
        ]
    },
    {
        "title": "Final Synthesis: The Unified Picture",
        "bullets": [
            "[Visual Concept: A single clean structural diagram linking formal limits, bounded feasibility, empirical scaling, and hardware architecture]",
            "1. Computability: Open-ended ascent across relative boundaries",
            "2. Feasibility: Staged reachability through polynomial-time verification",
            "3. Empirical Drivers: Logical scaling sustained by compounding hidden efficiency",
            "4. Architectural Response: Rising scalable workloads driving hardware toward programmable compute"
        ]
    },
    {
        "title": "Closing Takeaways",
        "bullets": [
            "A Structured Phenomenon: AI progress is neither pure hype nor a contradiction of theoretical limits",
            "The Unified Program: Intelligence emerges as a structured, open-ended process bounded by formal limits, propelled by empirical scaling drivers, and fundamentally reshaping system-level hardware consequences"
        ]
    }
]

def create_presentation(output_path):
    prs = Presentation()
    
    # 16:9 Aspect ratio
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    # slide_layouts[1] is Title and Content
    layout = prs.slide_layouts[1]
    
    for slide_data in slides_data:
        slide = prs.slides.add_slide(layout)
        
        # Set Title
        title_shape = slide.shapes.title
        title_shape.text = slide_data["title"]
        
        # Set Bullets
        body_shape = slide.placeholders[1]
        text_frame = body_shape.text_frame
        
        for i, bullet in enumerate(slide_data["bullets"]):
            if i == 0:
                p = text_frame.paragraphs[0]
            else:
                p = text_frame.add_paragraph()
            
            p.text = bullet.strip()
            
            # Simple indention logic
            if bullet.startswith("  ") or bullet.startswith("[Visual") or bullet[0].isdigit():
                p.level = 1
            else:
                p.level = 0

    prs.save(output_path)
    print(f"Native PPTX generated and saved to {output_path}")

if __name__ == '__main__':
    create_presentation("The_AI_Progress_Blueprint.pptx")
