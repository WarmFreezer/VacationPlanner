import VacationData

#class WebSearchAI:        
def SearchWeb(url, prompt):
    graph_config = {
        "lim": {
            "model": "ollama/llama3",
            "temperature": 0, 
            "format": "json", 
            "base_url": "http://localhost:11434",
        },
        "embeddings": {
            "model": "ollama/nomic-embed-text", 
            "base_url": "http://localhost:11434",
        },
        "verbose": True,
    }  
        
    smart_scraper_graph = SmartScraperGraph(
        prompt = prompt,
        source = url,
        config = graph_config
    )
        
    results = smart_scraper_graph.run()
    st.write(results)
        
    def SearchWeb():
        print("Unfinished - SearchWeb()")
        #Must create VacationData objects from the AI output