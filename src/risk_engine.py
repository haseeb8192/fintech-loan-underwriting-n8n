from typing import Dict, Any
from pydantic import BaseModel, Field


class ApplicantProfile(BaseModel):
    applicant_id: str
    monthly_income: float = Field(..., gt=0)
    existing_debt: float = Field(default=0.0, ge=0)
    requested_loan_amount: float = Field(..., gt=0)
    credit_score: int = Field(..., ge=300, le=850)


class UnderwritingDecision(BaseModel):
    decision: str  # APPROVED, REJECTED, HITL_REVIEW
    dti_ratio: float
    risk_tier: str
    notes: str


def evaluate_applicant_risk(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Evaluates loan applicant risk metrics using Debt-to-Income (DTI) 
    and credit tiering thresholds for automated underwriting workflows.
    """
    profile = ApplicantProfile(**data)
    
    # Calculate Debt-to-Income Ratio (DTI)
    dti = (profile.existing_debt / profile.monthly_income) * 100

    # Risk Boundaries & Fallback Rules
    if profile.credit_score >= 720 and dti < 35:
        return UnderwritingDecision(
            decision="APPROVED",
            dti_ratio=round(dti, 2),
            risk_tier="LOW_RISK",
            notes="Instant pre-approval: Optimal credit score and manageable DTI."
        ).model_dump()
        
    elif profile.credit_score < 580 or dti > 50:
        return UnderwritingDecision(
            decision="REJECTED",
            dti_ratio=round(dti, 2),
            risk_tier="HIGH_RISK",
            notes="Auto-rejection: Exceeds maximum risk exposure limits."
        ).model_dump()
        
    else:
        return UnderwritingDecision(
            decision="HITL_REVIEW",
            dti_ratio=round(dti, 2),
            risk_tier="MODERATE_RISK",
            notes="Borderline applicant: Dispatched to manual underwriter Slack gate."
        ).model_dump()
