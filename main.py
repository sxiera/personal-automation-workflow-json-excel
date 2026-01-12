import subprocess
import os
import sys

def run_step(script_name, description):
    print(f"\n{'='*60}")
    print(f"STEP: {description}")
    print(f"Running {script_name}...")
    print(f"{'='*60}\n")
    
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), script_name)
    
    if not os.path.exists(script_path):
        print(f"Error: Script {script_path} not found.")
        sys.exit(1)

    try:
        # Run the script and wait for it to complete
        result = subprocess.run([sys.executable, script_path], check=True, text=True)
        print(f"\n>> {script_name} completed successfully.")
        
    except subprocess.CalledProcessError as e:
        print(f"\n!! Error running {script_name}. Exit code: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"\n!! Unexpected error: {e}")
        sys.exit(1)

def main():
    print("Starting Automation Assessment Workflow...")
    
    # 1. Convert Input
    run_step("src/1_convert_input.py", "Converting Excel Input to JSON")
    
    # 2. Assess
    run_step("src/2_assess_opportunities.py", "Assessing Opportunities (Populating Attributes)")
    
    # 3. Audit
    run_step("src/3_audit_results.py", "Auditing Results (Context Check)")
    
    # 4. Generate Report
    run_step("src/4_generate_report.py", "Generating Final Excel Report")
    
    print(f"\n{'='*60}")
    print("WORKFLOW COMPLETED SUCCESSFULLY")
    print(f"{'='*60}\n")
    print("Output available at: src/final_assessment_result.xlsx")

if __name__ == "__main__":
    main()
