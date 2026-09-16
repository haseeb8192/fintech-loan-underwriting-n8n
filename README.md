# Autonomous FinTech Loan Underwriting & Risk Routing Engine

An event-driven backend service engineered to automate unstructured loan application intake, credit assessment, risk evaluation, and multi-tier applicant routing. Built to handle asynchronous processing with sub-2s execution latency and automated fallbacks.

---

## Business Problem
NBFCs and micro-lending platforms spend hundreds of manual engineering and operational hours reviewing unqualified leads and handling unstandardized applicant inputs. Manual triage introduces operational bottlenecks, inconsistent risk scoring, and high drop-off rates.

## System Architecture
```mermaid
flowchart TD
    A[Loan Ingestion / Webhook] --> B[FastAPI Gateway]
    B --> C[Pydantic Validation & Sanitization]
    C --> D[n8n Event Orchestrator]
    D --> E{LLM Extraction & Risk Scoring}
    E -->|Success| F[MongoDB State Store]
    E -->|Timeout / Rate Limit| G[Fallback Pipeline / Manual Review Queue]
    F --> H{Risk Score > Threshold}
    H -->|Approved| I[Automated Underwriter Notification / Dispatch]
    H -->|Flagged| J[Human-in-the-Loop Slack / Review Channel]
