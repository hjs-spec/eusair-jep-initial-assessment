# Case 3: Cross-Border Smart Traffic Coordination (TEN-T Network)

## Scenario Overview

This case demonstrates a cross-border traffic management system involving multiple AI agents across the EU's Trans-European Transport Network (TEN-T), with implications for public safety, emergency response, and infrastructure coordination.

**Participants**:
- **Netherlands**: Rijkswaterstaat congestion prediction AI (critical infrastructure)
- **Belgium**: Port of Antwerp logistics coordination AI (freight priority system)
- **Germany**: Autobahn real-time traffic AI (highway management)
- **Three Countries**: Traffic control center human operators (joint oversight)

**Flow**:
```
Congestion detected on major freight route
    ↓
Dutch traffic AI (Agent A) predicts cascading delays
    ↓
Agent A delegates freight prioritization to Belgian port AI (Agent B)
    ↓
Agent B delegates rerouting to German Autobahn AI (Agent C)
    ↓
Agent C implements traffic flow adjustments
    ↓
Three-country control center operators (Human) jointly monitor and confirm
```

## Regulatory Context (EU AI Act)

| Article | Requirement | Relevance to This Case |
|---------|-------------|------------------------|
| **Annex III, Art. 2** | Critical infrastructure AI is high-risk | Traffic management systems fall under Annex III |
| **Art. 27** | Fundamental rights impact assessment | Traffic decisions affect mobility rights, emergency access |
| **Art. 43** | Conformity assessment | System must undergo third-party conformity assessment |
| **Art. 60** | Testing in real-world conditions | TEN-T network qualifies for real-world testing provisions |
| **Art. 14** | Human oversight | Multi-country operators must maintain effective control |

## Accountability Challenge

If an emergency vehicle is delayed due to AI-coordinated traffic decisions:

- Was the Dutch congestion prediction AI's forecast inaccurate?
- Did the Belgian port AI prioritize freight over emergency access?
- Did the German Autobahn AI implement rerouting incorrectly?
- Did the human operators fail to override in time?

Without cross-system accountability, each country's agency can blame the others. With JEP, the complete decision chain across all three countries is recorded and verifiable.

## JEP Implementation

```
judge(Rijkswaterstaat_AI, {version: "4.1", authority: "congestion-prediction", network: "TEN-T-corridor-2"})
    → delegate(PortOfAntwerp_AI, {purpose: "freight-prioritization", emergency_override: false})
    → delegate(Autobahn_AI, {purpose: "reroute-implementation", affected_routes: ["A67", "A40"]})
    → terminate(JointOperators, {confirmation: true, override: false, timestamp: "2026-03-08T14:23:00Z"})
```

## Evidence Location

- Input scenario: `scenario.json`
- Expected JEP receipt: `expected-receipt.json`
- Mapping to EU AI Act: `mapping.md`
- Run script: `run.py`
- Verification: `verify.sh`
```

---

# 📁 eusair-demo/case3-transport/scenario.json

```json
{
  "case_id": "eusair-case3-transport-001",
  "title": "Cross-Border Emergency Vehicle Delay Incident",
  "description": "A coordinated traffic management response across three countries leads to delayed emergency vehicle access during a peak freight period.",
  
  "actors": [
    {
      "id": "rijkswaterstaat-ai",
      "type": "high-risk-ai",
      "jurisdiction": "Netherlands",
      "organization": "Rijkswaterstaat",
      "authority": "national_road_authority",
      "version": "4.1",
      "model_hash": "0x8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f",
      "certification": "TEN-T-critical-v2",
      "network_scope": ["A67", "A2", "N69"]
    },
    {
      "id": "port-of-antwerp-ai",
      "type": "logistics-coordination-ai",
      "jurisdiction": "Belgium",
      "organization": "Port of Antwerp-Bruges",
      "authority": "port_authority",
      "version": "3.2",
      "model_hash": "0x5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a",
      "certification": "CE-certified-logistics"
    },
    {
      "id": "autobahn-ai",
      "type": "traffic-management-ai",
      "jurisdiction": "Germany",
      "organization": "Autobahn GmbH",
      "authority": "federal_highway_authority",
      "version": "5.0",
      "model_hash": "0x2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e",
      "certification": "TEN-T-critical-v3"
    },
    {
      "id": "joint-control-operators",
      "type": "human-team",
      "members": [
        {
          "name": "Jan de Vries",
          "country": "Netherlands",
          "role": "Traffic Control Specialist",
          "station": "Rijkswaterstaat Verkeerscentrale"
        },
        {
          "name": "Marie Dubois",
          "country": "Belgium",
          "role": "Port Logistics Coordinator",
          "station": "Port of Antwerp Control Tower"
        },
        {
          "name": "Klaus Schmidt",
          "country": "Germany",
          "role": "Autobahn Traffic Manager",
          "station": "Verkehrszentrale Nordrhein-Westfalen"
        }
      ]
    }
  ],
  
  "incident_data": {
    "incident_id": "TEN-T-2026-03-08-001",
    "timestamp": "2026-03-08T14:15:00Z",
    "location": "A67 near Venlo, Netherlands-Germany border",
    "incident_type": "multi-vehicle_accident",
    "severity": "critical",
    "lanes_blocked": 2,
    "emergency_vehicles_dispatched": ["ambulance-1", "fire-engine-3", "police-2"],
    "emergency_eta_normal": "8 minutes"
  },
  
  "traffic_conditions": {
    "time_of_day": "14:15 (peak freight hour)",
    "day_of_week": "Tuesday",
    "current_traffic_density": "high",
    "port_schedule": {
      "port_of_antwerp": "peak_departure_window",
      "ships_departing": 12,
      "trucks_in_queue": 450,
      "just_in_time_deliveries": true
    },
    "autobahn_status": {
      "a40_congestion": "moderate",
      "a67_incident": "severe",
      "alternative_routes": ["A2 via Netherlands", "A57 via Germany"]
    }
  },
  
  "execution_flow": [
    {
      "step": 1,
      "actor": "rijkswaterstaat-ai",
      "action": "detect_incident",
      "timestamp": "2026-03-08T14:15:30Z",
      "detection_method": "camera + sensor fusion",
      "confidence": 0.98,
      "output": {
        "incident_detected": true,
        "predicted_congestion_duration": "45 minutes",
        "affected_routes": ["A67 southbound", "N69 local roads"],
        "cascading_delay_risk": "high"
      }
    },
    {
      "step": 2,
      "actor": "rijkswaterstaat-ai",
      "action": "analyze_freight_impact",
      "timestamp": "2026-03-08T14:15:45Z",
      "analysis": {
        "port_of_antwerp_impact": "likely_delays",
        "just_in_time_disruption": "high_risk",
        "alternative_freight_routes": ["A2 via Eindhoven", "A57 via Germany"]
      }
    },
    {
      "step": 3,
      "actor": "rijkswaterstaat-ai",
      "action": "delegate",
      "to": "port-of-antwerp-ai",
      "purpose": "freight_priority_coordination",
      "incident_context": {
        "location": "A67 border crossing",
        "duration_estimate": "45 minutes",
        "affected_port_operators": ["DP World", "PSA Antwerp"]
      },
      "timestamp": "2026-03-08T14:16:00Z"
    },
    {
      "step": 4,
      "actor": "port-of-antwerp-ai",
      "action": "assess_freight_priority",
      "timestamp": "2026-03-08T14:16:15Z",
      "assessment": {
        "ships_at_berth": 8,
        "loading_completion_times": ["15min", "25min", "40min", "55min"],
        "critical_departures": ["container_ship_CMA_CGM_302", "ro_ro_ferry_P&O_177"],
        "flexible_departures": ["bulk_carrier_3", "container_ship_4"]
      }
    },
    {
      "step": 5,
      "actor": "port-of-antwerp-ai",
      "action": "delegate",
      "to": "autobahn-ai",
      "purpose": "reroute_freight_traffic",
      "reroute_parameters": {
        "priority_vehicles": ["container_ship_302_trucks", "ferry_177_trucks"],
        "flexible_vehicles": ["bulk_carrier_3_trucks"],
        "time_sensitivity": "high_for_priority",
        "incident_location": "A67 near Venlo"
      },
      "timestamp": "2026-03-08T14:16:30Z"
    },
    {
      "step": 6,
      "actor": "autobahn-ai",
      "action": "calculate_alternative_routes",
      "timestamp": "2026-03-08T14:16:45Z",
      "route_options": [
        {
          "route": "A67 → A40 → A57",
          "distance_km": 45,
          "time_minutes": 38,
          "capacity": "moderate",
          "emergency_access": "maintained"
        },
        {
          "route": "A67 → N69 → A2",
          "distance_km": 52,
          "time_minutes": 42,
          "capacity": "low",
          "emergency_access": "compromised_on_N69"
        },
        {
          "route": "A67 → A40 → A3",
          "distance_km": 58,
          "time_minutes": 48,
          "capacity": "high",
          "emergency_access": "fully_maintained"
        }
      ]
    },
    {
      "step": 7,
      "actor": "autobahn-ai",
      "action": "implement_rerouting",
      "timestamp": "2026-03-08T14:17:00Z",
      "implementation": {
        "selected_route": "A67 → A40 → A57",
        "dynamic_signs_updated": true,
        "navigation_systems_notified": ["TomTom", "Google Maps", "Waze", "Truck GPS networks"],
        "priority_lanes_activated": false,
        "note": "Priority lanes not activated - emergency vehicle protocol not triggered"
      }
    },
    {
      "step": 8,
      "actor": "autobahn-ai",
      "action": "return_confirmation",
      "to": "port-of-antwerp-ai",
      "timestamp": "2026-03-08T14:17:10Z",
      "confirmation": {
        "reroute_complete": true,
        "priority_vehicles_handled": true,
        "flexible_vehicles_handled": true,
        "estimated_time_saved": "12 minutes for priority vehicles"
      }
    },
    {
      "step": 9,
      "actor": "port-of-antwerp-ai",
      "action": "return_coordination_result",
      "to": "rijkswaterstaat-ai",
      "timestamp": "2026-03-08T14:17:20Z",
      "result": {
        "freight_coordination_complete": true,
        "critical_departures_protected": true,
        "flexible_departures_delayed": ["bulk_carrier_3", "container_ship_4"],
        "estimated_delay": "25 minutes for flexible departures"
      }
    },
    {
      "step": 10,
      "actor": "rijkswaterstaat-ai",
      "action": "notify_emergency_services",
      "timestamp": "2026-03-08T14:17:30Z",
      "notification": {
        "emergency_access_status": "maintained on A40, A57",
        "incident_location_eta": "updated to 15 minutes",
        "recommended_route": "A40 direct to incident",
        "priority_override_available": true
      }
    },
    {
      "step": 11,
      "actor": "joint-control-operators",
      "action": "joint_review",
      "timestamp": "2026-03-08T14:18:00Z",
      "review_meeting": "emergency_coordination_call",
      "participants": ["Jan de Vries", "Marie Dubois", "Klaus Schmidt"],
      "duration_minutes": 3,
      "discussion_summary": "All operators confirm AI decisions appropriate given freight priority. Emergency services notified. Monitoring situation."
    },
    {
      "step": 12,
      "actor": "joint-control-operators",
      "action": "confirm_actions",
      "timestamp": "2026-03-08T14:21:00Z",
      "confirmation": {
        "confirmed_by": "all_three_operators",
        "override_issued": false,
        "override_reason": "none_needed",
        "next_review": "in_15_minutes_or_if_situation_changes"
      }
    }
  ],
  
  "final_outcome": {
    "incident_resolution_time": "47 minutes",
    "emergency_vehicle_arrival": "15 minutes (delayed by 7 minutes)",
    "freight_impact": {
      "critical_departures": "on_time",
      "flexible_departures": "delayed_25_minutes"
    },
    "human_override_used": false,
    "investigation_required": true,
    "responsible_coordinator": "joint-control-operators",
    "contributing_ais": ["rijkswaterstaat-ai", "port-of-antwerp-ai", "autobahn-ai"],
    "jep_receipt": "expected-receipt.json"
  }
}
```

---

# 📁 eusair-demo/case3-transport/mapping.md

```markdown
# EU AI Act Mapping: Case 3 - Cross-Border Smart Traffic Coordination

| Article | Requirement | How JEP Addresses It | Evidence |
|---------|-------------|----------------------|----------|
| **Annex III, Art. 2** | Critical infrastructure AI | All three traffic AIs identified as high-risk in `judge` primitives | `scenario.json` - actors[0].type, actors[2].type |
| **Art. 27** | Fundamental rights impact | Emergency vehicle delay implicates right to life, mobility | `scenario.json` - emergency_vehicles_dispatched, final_outcome.emergency_vehicle_arrival |
| **Art. 43** | Conformity assessment | All AIs have certification records in actor definitions | `scenario.json` - actors[0].certification, actors[2].certification |
| **Art. 60** | Real-world testing | TEN-T network qualifies under Art. 60 provisions | Entire scenario simulates real-world conditions |
| **Art. 14** | Human oversight | Three-country operator team jointly reviews and confirms | `scenario.json` - steps 11, 12 |

## Detailed Mapping

### Annex III, Article 2: Critical Infrastructure
Traffic management systems for major transport networks are explicitly listed as high-risk AI under Annex III. All three AIs in this case (Netherlands, Belgium, Germany) are properly identified with their certifications, ensuring traceability of compliance.

### Article 27: Fundamental Rights Impact Assessment
The delay of emergency vehicles potentially impacts the right to life and health (EU Charter of Fundamental Rights, Article 2 & 3). The JEP receipt records:
- When the incident was detected
- What AI decisions were made
- Whether human operators had opportunity to override
- The actual arrival time of emergency vehicles

This provides essential evidence for any subsequent fundamental rights investigation.

### Article 43: Conformity Assessment
Each AI system includes its certification status in the actor definition. The JEP receipt chains these certifications together, proving that all systems in the decision chain were properly assessed before deployment.

### Article 60: Testing in Real-World Conditions
The TEN-T network is an ideal candidate for real-world testing under Article 60. This scenario demonstrates how JEP can:
- Track decisions across multiple jurisdictions
- Provide auditable evidence for regulatory review
- Enable post-incident analysis without compromising safety

### Article 14: Human Oversight
Critical insight: the human operators did NOT override the AI, but they DID review and confirm. The JEP receipt proves:
- Operators were notified (step 10)
- They held a joint review (step 11)
- They explicitly confirmed the AI decisions (step 12)

This demonstrates "meaningful human oversight" as required by Article 14—not just rubber-stamping, but informed confirmation.
```

---

# 📁 eusair-demo/case3-transport/run.py

```python
#!/usr/bin/env python3
"""
Run Case 3: Cross-Border Smart Traffic Coordination
"""

import json
import sys
from pathlib import Path

# Add JEP core to path
sys.path.append(str(Path(__file__).parent.parent.parent / "src"))

from aip_jep.compliance_demo import process_scenario
from aip_jep.crypto import sign_receipt

def main():
    # Load scenario
    with open("scenario.json", "r") as f:
        scenario = json.load(f)
    
    print(f"\n{'='*60}")
    print(f"Running Case 3: {scenario['title']}")
    print(f"{'='*60}\n")
    
    print(f"Description: {scenario['description']}")
    print(f"\nActors involved:")
    for actor in scenario['actors']:
        if actor['type'] != 'human-team':
            print(f"  - {actor['id']} ({actor['type']}, {actor['jurisdiction']})")
        else:
            print(f"  - Joint Control Operators (human, Netherlands/Belgium/Germany)")
    
    print(f"\nIncident: {scenario['incident_data']['incident_type']}")
    print(f"Location: {scenario['incident_data']['location']}")
    print(f"Emergency vehicles dispatched: {', '.join(scenario['incident_data']['emergency_vehicles_dispatched'])}")
    
    # Process the scenario using JEP
    print(f"\n{'→'*40}")
    print("Processing with JEP...")
    print(f"{'→'*40}")
    
    receipt = process_scenario(scenario)
    
    # Add cryptographic signature
    signed_receipt = sign_receipt(receipt)
    
    # Save expected receipt
    with open("expected-receipt.json", "w") as f:
        json.dump(signed_receipt, f, indent=2)
    
    print(f"\n✓ JEP Receipt generated and saved to expected-receipt.json")
    print(f"\nFinal outcome:")
    print(f"  - Incident resolution: {scenario['final_outcome']['incident_resolution_time']}")
    print(f"  - Emergency vehicle arrival: {scenario['final_outcome']['emergency_vehicle_arrival']}")
    print(f"  - Human override used: {scenario['final_outcome']['human_override_used']}")
    print(f"  - Investigation required: {scenario['final_outcome']['investigation_required']}")
    
    print(f"\n{'='*60}")
    print("Case 3 completed successfully")
    print(f"{'='*60}\n")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

---

# 📁 eusair-demo/case3-transport/verify.sh

```bash
#!/bin/bash
# Verification script for Case 3

echo "=========================================="
echo "Verifying Case 3: Cross-Border Smart Traffic Coordination"
echo "=========================================="

# Check if expected receipt exists
if [ ! -f "expected-receipt.json" ]; then
    echo "❌ expected-receipt.json not found. Run run.py first."
    exit 1
fi

# Run JEP verification
python3 ../../src/aip_jep/verify_sandbox.py --receipt expected-receipt.json

if [ $? -eq 0 ]; then
    echo "✅ Case 3 verification passed"
else
    echo "❌ Case 3 verification failed"
    exit 1
fi

# Additional transport-specific verification
echo ""
echo "Transport compliance checks:"
echo "-----------------------------"

# Check if human oversight recorded
if grep -q "joint-control-operators.*confirm" scenario.json; then
    echo "✅ Multi-country human oversight recorded"
else
    echo "⚠️  Human oversight not clearly recorded"
fi

# Check if emergency services notified
if grep -q "notify_emergency_services" scenario.json; then
    echo "✅ Emergency services notification tracked"
else
    echo "⚠️  Emergency notification not found"
fi

# Check if alternative routes calculated
if grep -q "calculate_alternative_routes" scenario.json; then
    echo "✅ Route planning transparency maintained"
else
    echo "⚠️  Route planning details missing"
fi

# Check for fundamental rights implications
if grep -q "emergency_vehicle_arrival" scenario.json; then
    echo "✅ Emergency response tracked (fundamental rights)"
else
    echo "⚠️  Emergency response data missing"
fi

echo ""
echo "=========================================="
```

---
