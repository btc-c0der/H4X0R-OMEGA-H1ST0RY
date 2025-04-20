"""
L0pht Heavy Industries Module for the OMEGA HACKER HISTORICAL MUSEUM
"""

def get_lopht_data():
    """Returns information about L0pht Heavy Industries history."""
    return {
        "name": "L0pht Heavy Industries",
        "emoji": "🔐",
        "years_active": "1992-2000",
        "location": "Boston, Massachusetts",
        "founders": [
            "Brian Oblivion (Brian Hassick)",
            "Count Zero (John Lester)",
            "Dildog (Christien Rioux)",
            "Kingpin (Joe Grand)",
            "Silicosis (Paul Nash)",
            "Space Rogue (Cris Thomas)",
            "Stefan (Stefan Wuensch)",
            "Weld Pond (Chris Wysopal)",
            "Mudge (Peiter Zatko)"
        ],
        "key_products": [
            {
                "name": "L0phtCrack",
                "description": "Password auditing and recovery tool for Windows NT",
                "year": 1997
            },
            {
                "name": "POCSAG Decoder",
                "description": "Hardware decoder for pager messages",
                "year": 1995
            },
            {
                "name": "Security Advisories",
                "description": "Published numerous security vulnerabilities and advisories",
                "year": "1992-2000"
            }
        ],
        "achievements": [
            {
                "name": "Congressional Testimony",
                "description": "Testified before the US Senate on critical cybersecurity vulnerabilities",
                "year": 1998,
                "quote": "We could shut down the entire Internet in 30 minutes"
            },
            {
                "name": "Responsible Disclosure",
                "description": "Pioneers of responsible vulnerability disclosure practices",
                "year": "1992-2000"
            },
            {
                "name": "First US Hackerspace",
                "description": "One of the first viable hackerspaces in the United States",
                "year": 1992
            }
        ],
        "legacy": [
            {
                "event": "Merged with @stake",
                "year": 2000,
                "description": "Completed transition from underground organization to security company"
            },
            {
                "event": "Symantec acquisition",
                "year": 2004,
                "description": "Symantec acquired @stake"
            },
            {
                "event": "L0phtCrack released as open source",
                "year": 2021,
                "description": "L0phtCrack tool made freely available as open source software"
            }
        ],
        "advisories": [
            "Windows NT password hashing weaknesses",
            "Windows 95/98 vulnerabilities",
            "Sendmail vulnerabilities",
            "Multiple TCP/IP stack vulnerabilities",
            "Various network protocol weaknesses"
        ]
    }

def get_lopht_template():
    """Returns markdown template with L0pht Heavy Industries history."""
    return """# 🔐 L0PHT H34VY INDU5TR1E5

## H4CK3R TH1NK T4NK

L0pht Heavy Industries was one of the most influential hacker collectives of the 1990s, operating from 1992 to 2000 in Boston, Massachusetts.

## K3Y M3MB3R5
- **Brian Oblivion** - Founding member
- **Count Zero** - Founding member  
- **Dildog** - Developer of L0phtCrack
- **Kingpin** - Hardware specialist
- **Mudge** - Security researcher
- **Space Rogue** - Published Hacker News Network
- **Weld Pond** - Windows security expert

## F4M0U5 PR0DUCT5
- **L0phtCrack** - Windows NT password cracker
- **Whacked Mac Archives** - Collection of Macintosh software
- **POCSAG Decoder** - Hardware for decoding pager messages
- **Black Crawling System Archives** - Historical hacker archives

## H15T0R1C4L 1MP4CT
- **1998 Congressional Testimony** - "We could shut down the entire Internet in 30 minutes"
- **Pioneered responsible disclosure** of security vulnerabilities
- **First major US hackerspace** predating modern movement
- **Influenced US cybersecurity policy** through direct government engagement"""

def get_lopht_advisory_template():
    """Returns a sample L0pht security advisory template."""
    return """# L0PHT S3CUR1TY 4DV1S0RY

## ADVISORY: Windows NT Passwords Cryptographically Weak

**Release Date**: March 1997
**Severity**: Critical
**Systems Affected**: All Windows NT systems

## DESCRIPTION
The authentication mechanism used in Windows NT is cryptographically weak and allows attackers to brute force passwords regardless of password complexity.

## DETAILS
Microsoft's implementation of the LM hash algorithm:
1. Converts all lowercase to uppercase
2. Pads passwords to 14 characters
3. Splits the password into two 7 character chunks
4. Creates a hash from each chunk separately

This implementation significantly reduces the complexity of cracking passwords as each 7-character chunk can be attacked independently.

## PROOF OF CONCEPT
The L0phtCrack tool demonstrates this vulnerability by recovering Windows NT password hashes at high speed using standard hardware.

## RECOMMENDATION
- Use NTLM instead of LM hash where possible
- Implement strong password policies
- Consider additional authentication factors
- Monitor for unauthorized access attempts

Discovered by The L0pht - 1997""" 