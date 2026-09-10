# 🏦 Event-Driven FinTech Underwriting & Risk-Routing Engine

A production-ready workflow automation pipeline built with **n8n**, integrating automated financial ratio evaluations, risk scoring, and **LLM fallback orchestration** for intelligent loan decisioning.

---

## 📌 Architecture Overview  

```mermaid
graph TD
    A[Inbound Loan Application Webhook] --> B[Parse & Validate Financial Data]
    B --> C{Rule-based Ratio Check}
    C -->|High Confidence Pass/Fail| D[Automated Decision & CRM Sync]
    C -->|Borderline / Complex Edge Case| E[LLM Structured Risk Assessment]
    E --> F[Generate Structured JSON Risk Matrix]
    F --> D
    D --> G[Disbursement Trigger & Multi-Channel Alert]
