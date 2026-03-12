# Roles que queremos buscar
TARGET_ROLES = [
    "portfolio analyst",
    "risk analyst",
    "trading analyst",
    "market risk analyst",
    "financial risk analyst",
    "investment risk analyst",
    "commodity analyst",
    "energy trading analyst",
    "trading risk analyst",
    "junior quant analyst",
    "quantitative analyst",
    "quantitative risk analyst",
    "financial data analyst"
]

# Palabras que indican nivel junior
LEVEL_KEYWORDS = [
    "intern",
    "graduate",
    "entry",
    "junior",
    "analyst"
]

# Palabras que queremos excluir
EXCLUDE_KEYWORDS = [
    "senior",
    "manager",
    "director",
    "lead",
    "principal"
]

# Ubicaciones objetivo
TARGET_LOCATIONS = [
    "switzerland",
    "uk",
    "netherlands",
    "germany",
    "denmark",
    "sweden",
    "norway",
    "france",
    "spain",
    "singapore",
    "hong kong",
    "united states"
]

# Empresas objetivo
TARGET_COMPANIES = [
    "rwe",
    "statkraft",
    "uniper",
    "engie",
    "edf",
    "shell",
    "bp",
    "blackrock",
    "gunvor",
    "mercuria",
    "vitol",
    "trafigura"
]

# Fuentes de búsqueda
JOB_SOURCES = [
    "linkedin",
    "indeed",
    "efinancialcareers",
    "glassdoor"
]



import config

def main():
    print("Job Hunter Bot starting...\n")

    print("Target roles:")
    for role in config.TARGET_ROLES:
        print("-", role)

    print("\nTarget locations:")
    for location in config.TARGET_LOCATIONS:
        print("-", location)

    print("\nTarget companies:")
    for company in config.TARGET_COMPANIES:
        print("-", company)


if __name__ == "__main__":
    main()
