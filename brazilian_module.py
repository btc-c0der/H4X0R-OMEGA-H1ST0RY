"""
Brazilian Hacker History Module for the OMEGA HACKER HISTORICAL MUSEUM
"""

def get_br_hacker_data():
    """Returns information about Brazilian hacker history."""
    return {
        "groups": {
            "BR.Gov": {
                "name": "Brazilian Digital Underground",
                "emoji": "🇧🇷",
                "description": "Brazilian hacktivists focused on government transparency",
                "era": "2000s-2010s"
            },
            "LulzSec BR": {
                "name": "LulzSec Brazil",
                "emoji": "🏴‍☠️",
                "description": "Brazilian branch of LulzSec, known for operations against government sites",
                "era": "2011-2012" 
            }
        },
        "incidents": [
            {
                "year": 2011,
                "name": "Operation Anti-Security (AntiSec)",
                "description": "Brazilian hackers participated in global hacktivist movement"
            },
            {
                "year": 2013,
                "name": "World Cup Protests",
                "description": "Hacktivist operations during protests against FIFA World Cup spending"
            },
            {
                "year": 2016,
                "name": "Political Tensions",
                "description": "Increased hacktivism during political transition period"
            },
            {
                "year": 2019,
                "name": "Government Database Leaks",
                "description": "Several breaches of Brazilian government databases"
            }
        ]
    }

def get_br_template():
    """Returns markdown template with Brazilian hacker history."""
    return """# 🇧🇷 Brazilian Hacker History

## Digital Activism in Brazil

Brazil has a unique hacker culture influenced by political and economic factors.

## Key Events
- **2011**: LulzSec Brazil targets government sites
- **2013**: Hacktivists support World Cup protests
- **2016**: Political transition period sees rise in hacktivism
- **2020**: Increased focus on government transparency

## Notable Operations
- **Operação Falcão Negro** - Targeting corruption
- **Vazamento BR** - Database leaks exposing government information
- **Projetos de Transparência** - Tools for monitoring political activities

## Cultural Impact
The Brazilian hacker scene blends global hacker culture with local political activism, often focusing on government transparency and anti-corruption.""" 