const { createApp } = Vue;

createApp({
    data() {
        return {
            filterKey: "",
            filterValue: "",
            columns: ["Registro_ANS", "CNPJ", "Razao_Social", "Nome_Fantasia", "Modalidade", "Logradouro","Bairro", "Cidade", "UF", "CEP", "Representante", "Regiao_de_Comercializacao", "Data_Registro_ANS"],
            results: []
        };
    },
    methods: {
        async fetchData() {
            if (!this.filterKey || !this.filterValue) {
                alert("Selecione uma coluna e digite um valor para filtrar.");
                return;
            }

            try {
                const response = await axios.get("http://127.0.0.1:5000/search_cadop", {
                    params: { [this.filterKey]: this.filterValue }
                });
                this.results = response.data;
            } catch (error) {
                console.error("Erro ao buscar dados:", error);
                alert("Erro ao buscar dados. Verifique o servidor.");
            }
        }
    }
}).mount("#app");