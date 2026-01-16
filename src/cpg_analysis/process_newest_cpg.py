import json
import pandas as pd

input_file = '/Users/bimaaristo/MH/revise/cpg_newest.json'
output_file = '/Users/bimaaristo/MH/newest/CPG-Research (1)-Rewritten.xlsx'

# Define the mapping logic based on Key Player and partial text matching
# formatted as: (KeyPlayer_substring, Topic_substring) -> { 'Key Topics': ..., 'Business Case': ..., 'How (Technical)': ... }
rewrites = [
    {
        'match': lambda item: 'P&G' in item['Key Player'],
        'data': {
            'Key Topics & Issues': 'AI-Driven Marketing Optimization',
            'Business Case': 'Cut ad testing optimization time from weeks to days. Reduce costs. Enable fully autonomous, hyper-personalized campaign orchestration.',
            'How (Technical)': 'Layered AI architecture: Generative models for creative ideation, Predictive analytics (Random Forest, XGBoost) for variant testing, and Bayesian bandit models for real-time traffic allocation.'
        }
    },
    {
        'match': lambda item: 'Unilever' in item['Key Player'] and 'Product shoots' in item['Key Topics & Issues'],
        'data': {
            'Key Topics & Issues': 'AI-Driven Content Creation',
            'Business Case': 'Reinvent product shoots to create high-quality product imagery faster and more cost-effectively. Execute campaigns with greater creativity and autonomy.',
            'How (Technical)': 'Digital Twin technology (Real-Time 3D, Nvidia Omniverse, OpenUSD) creates accurate 3D replicas integrated into AI-enhanced creative workflows.'
        }
    },
    {
        'match': lambda item: 'Nestle x IBM' in item['Key Player'],
        'data': {
            'Key Topics & Issues': 'Product Innovation & Recipe Formulation',
            'Business Case': 'Unlock new opportunities by connecting proprietary data. Better manage tradeoffs between ingredients, nutrition, cost, and sustainability in product development.',
            'How (Technical)': 'Generative AI (LLM + RAG) fine-tuned on a fit-for-purpose chemical language model using proprietary corpus.'
        }
    },
    {
        'match': lambda item: 'Unilever' in item['Key Player'] and 'Ice Cream' in item['Key Topics & Issues'],
        'data': {
            'Key Topics & Issues': 'Supply Chain Optimization & Demand Forecasting',
            'Business Case': 'Improve forecast accuracy (e.g., ~10% in Sweden). Boost orders and sales (up to 30%) by understanding inventory in real-time.',
            'How (Technical)': 'AI analysis of real-time inventory, weather, and sales data from 100,000 "AI-enabled" retail freezers.'
        }
    },
    {
        'match': lambda item: 'Mondelez' in item['Key Player'],
        'data': {
            'Key Topics & Issues': 'Scalable Marketing Content',
            'Business Case': 'Enable content creation (text, image, video) at scale while ensuring brand safety and legal compliance. Support personalization and A/B testing.',
            'How (Technical)': 'Generative-AI marketing platform incorporating multimodal LLM capabilities.'
        }
    },
    {
        'match': lambda item: 'Reckitt' in item['Key Player'],
        'data': {
            'Key Topics & Issues': 'Product Emission Analysis',
            'Business Case': 'Efficiently analyze massive datasets for product emissions to drive sustainability.',
            'How (Technical)': 'AI analysis of 300,000+ data points.'
        }
    },
    {
        'match': lambda item: 'Heineken' in item['Key Player'] and 'Customer-centric' in item['Key Topics & Issues'],
        'data': {
            'Key Topics & Issues': 'Sales Empowerment & Advisory',
            'Business Case': 'Increase sales productivity by transforming sales reps into business advisors. Predict best actions and select right touchpoints based on value potential.',
            'How (Technical)': 'AIDDA (AI Data-Driven Advisor) embedded into CRM applications and B2B platforms, using predictive analytics to identify next-best actions.'
        }
    },
    {
        'match': lambda item: 'Heineken' in item['Key Player'] and 'Promo Advisor' in item['Key Topics & Issues'],
        'data': {
            'Key Topics & Issues': 'Promotion Optimization',
            'Business Case': 'Boost sales and ROI by enabling optimal planning of targeted promotions.',
            'How (Technical)': 'Promo Advisor (ML-based) featuring: Decomposer (historical analysis), Simulator (scenario testing), and Optimiser (constraint-based planning).'
        }
    }
]

try:
    with open(input_file, 'r') as f:
        data = json.load(f)

    processed_data = []
    for item in data:
        new_item = item.copy()
        
        # Apply rewrite if match found
        for rule in rewrites:
            if rule['match'](item):
                new_item.update(rule['data'])
                break
                
        processed_data.append(new_item)

    # Convert to DataFrame
    df = pd.DataFrame(processed_data)
    
    # Ensure correct column order
    columns = [
        "Documentation Date", 
        "Key Player", 
        "Key Topics & Issues", 
        "Business Case", 
        "How (Technical)", 
        "Demo", 
        "Source", 
        "Relevance"
    ]
    df = df[columns]
    
    # Save to Excel
    df.to_excel(output_file, index=False)
        
    print(f"Successfully processed {len(df)} rows to {output_file}")

except Exception as e:
    print(f"Error processing data: {e}")
