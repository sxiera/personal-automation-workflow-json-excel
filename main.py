
from src.pipeline import (
    step1_convert_input,
    step2_assess_opportunities,
    step3_audit_results,
    step4_generate_report
)

def run_step(module, description):
    print(f"\n{'='*60}")
    print(f"STEP: {description}")
    print(f"Running {module.__name__}...")
    print(f"{'='*60}\n")
    
    try:
        module.run()
        print(f"\n>> {module.__name__} completed successfully.")
    except Exception as e:
        print(f"\n!! Error running {module.__name__}: {e}")
        exit(1)

def main():
    print("Starting Automation Assessment Workflow...")
    
    # 1. Convert Input
    run_step(step1_convert_input, "Converting Excel Input to JSON")
    
    # 2. Assess
    run_step(step2_assess_opportunities, "Assessing Opportunities (Populating Attributes)")
    
    # 3. Audit
    run_step(step3_audit_results, "Auditing Results (Context Check)")
    
    # 4. Generate Report
    run_step(step4_generate_report, "Generating Final Excel Report")
    
    print(f"\n{'='*60}")
    print("WORKFLOW COMPLETED SUCCESSFULLY")
    print(f"{'='*60}\n")
    print("Output available at: data/misc/final_assessment_result.xlsx")

if __name__ == "__main__":
    main()
