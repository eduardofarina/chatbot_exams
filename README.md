# 🤖 AI Medical Report Assistant

## Overview
The **AI Medical Report Assistant** is a Streamlit-based chatbot application designed to assist medical professionals in reviewing and analyzing medical reports. Leveraging advanced language models, the application classifies reports into categories (Pathology, Radiology, Genetics, Laboratory), answers clinical queries, and escalates uncertain cases to human specialists.

---

## Features
- **Report Classification**: Automatically identifies and categorizes reports.
- **Interactive Q&A**: Answers medical queries based on the report content.
- **Human Escalation**: Identifies uncertain cases and escalates to human specialists.
- **User-Friendly Interface**: Intuitive Streamlit web interface for seamless interaction.

---

## Technical Components

### Frontend
- **Streamlit**: For a simple, interactive web UI.

### Backend
- **Language Models**: Groq (Llama 3.2-1B-preview).
- **Agents**: Specialized agents for Pathology, Radiology, Genetics, and Laboratory reports.
- **Toolkits**: Integrated tools such as DuckDuckGo for extended capabilities.

### Project Structure
```bash
├── agents.py                # Specialized medical report agents
├── llm.py                   # Language model configuration
├── main.py                  # Streamlit application entry point
├── prompts.py               # Prompts and instructions for the LLM
└── streamlit_aux.py         # Auxiliary Streamlit configurations
```

---

## Installation & Setup

### Prerequisites
- Python 3.9+
- Groq API Key

### Configuration
Set your Groq API key as an environment variable:
```bash
export GROQ_API_KEY='your_groq_api_key'
```

---

## Running the Application
```bash
streamlit run main.py
```

Visit `http://localhost:8501` to interact with the chatbot.

---

## Usage
- Input your medical report query through text.
- The application classifies and processes the report.
- View clear, concise answers or escalation messages as appropriate.

---

## Future Enhancements
- Integration with hospital systems for direct data access.
- Expanded agent capabilities with additional medical specializations.
- Enhanced voice interaction features.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

© 2025 AI Medical Report Assistant

---

# 🤖 Assistente de Laudos Médicos com IA

## Visão Geral
O **Assistente de Laudos Médicos com IA** é uma aplicação chatbot baseada em Streamlit, projetada para auxiliar profissionais médicos na revisão e análise de laudos médicos. Utilizando modelos de linguagem avançados, o aplicativo classifica laudos em categorias (Patologia, Radiologia, Genética, Laboratório), responde a perguntas clínicas e escala casos incertos para especialistas humanos.

---

## Funcionalidades
- **Classificação de Laudos**: Identifica e categoriza automaticamente os laudos.
- **Perguntas e Respostas Interativas**: Responde a consultas médicas baseadas no conteúdo do laudo.
- **Escalonamento Humano**: Identifica casos incertos e escala para especialistas humanos.
- **Interface Intuitiva**: Interface web Streamlit amigável e de fácil uso.

---

## Componentes Técnicos

### Frontend
- **Streamlit**: Para uma interface web simples e interativa.

### Backend
- **Modelos de Linguagem**: Groq (Llama 3.2-1B-preview).
- **Agentes**: Agentes especializados para laudos de Patologia, Radiologia, Genética e Laboratório.
- **Toolkits**: Ferramentas integradas como DuckDuckGo para funcionalidades ampliadas.

### Estrutura do Projeto
```bash
├── agents.py                # Agentes especializados em laudos médicos
├── llm.py                   # Configuração do modelo de linguagem
├── main.py                  # Ponto de entrada da aplicação Streamlit
├── prompts.py               # Prompts e instruções para o modelo de linguagem
└── streamlit_aux.py         # Configurações auxiliares do Streamlit
```

---

## Instalação e Configuração

### Pré-requisitos
- Python 3.9+
- Chave API Groq

### Configuração
Defina sua chave API Groq como variável de ambiente:
```bash
export GROQ_API_KEY='sua_chave_api_groq'
```

---

## Execução da Aplicação
```bash
streamlit run main.py
```

Acesse `http://localhost:8501` para interagir com o chatbot.

---

## Uso
- Insira sua consulta sobre laudos médicos através do texto.
- O aplicativo classifica e processa o laudo.
- Receba respostas claras e concisas ou mensagens de escalonamento conforme apropriado.

---

## Melhorias Futuras
- Integração com sistemas hospitalares para acesso direto a dados.
- Capacidades ampliadas dos agentes com especializações médicas adicionais.
- Funcionalidades aprimoradas para interação por voz.

---

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

---

© 2025 Assistente de Laudos Médicos com IA

