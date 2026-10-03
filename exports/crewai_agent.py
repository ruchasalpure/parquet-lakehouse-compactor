from crewai import Agent

parquet_lakehouse_compactor = Agent(
    role="Parquet Lakehouse Compactor",
    goal="Deliver high-precision autonomous Parquet Lakehouse Compactor operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
