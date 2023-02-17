<template>
	<div>
		<v-sheet width="700" class="mx-auto pt-15">
			<h1 color="primary">Cadastro de quarto</h1>
			<AlertaCriado v-show="msg" :msg="msg"/>
			<v-form @submit="addNewQuarto">
				<v-text-field id="nome" v-model="nome" type="text" name="name" placeholder="Digite o seu nome">
				</v-text-field>
				<v-text-field id="cidade" v-model="cidade" type="text" name="cidade" placeholder="Digite a cidade">
				</v-text-field>
				<v-text-field id="valor" v-model="valor" type="text" name="valor" placeholder="Digite o valor do aluguel">
				</v-text-field>
				<v-textarea id="descricao" v-model="description" type="text" name="descricao" placeholder="Descreva o quarto">
				</v-textarea>
				<v-text-field
					v-model="imagem"
					placeholder="Insira a url de uma foto do quarto"
				>
				</v-text-field>
				<v-btn type="submit" block class="ma-2" color="#5DCAD1" >Cadastrar</v-btn>
			</v-form>
		</v-sheet>
	</div>
</template>
<script>
import AlertaCriado from "./AlertaCriado.vue";
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"
import QuartosApi from "@/api/quarto.api.js"

export default {
		components: {
		AlertaCriado
	},
	props: {
    formLabel: {
      type: String,
      default: "",
    },
	},
	emits: ["newQuarto"],
	data() {
		return {
			title: "",
			nomes: null,
			bairros: null,
			valores: null,
			descricoes: null,
			imagens: null,
			nome: null,
			bairro: null,
			valor: null,
			descricao: null,
			imagem: null,
			msg: null,
		};
	},
	computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
}	
,
	// mounted(){
	// 	//this.getCadastros()
	// },
	// methods: {
		// async getCadastros() {
		// 	const req = await fetch("http://localhost:3000/dados");
		// 	const data = await req.json();
			
			// this.nomes = data.nomes;
			// this.cidades = data.cidades;
			// this.valores = data.valores;
			// this.descricoes = data.descricoes;
		//
		// async createCadastro(e) {
		// 	e.preventDefault();
		// 	const data = {
		// 		nome: this.nome,
		// 		cidade: this.cidade,
		// 		valor: this.valor,
		// 		descricao: this.descricao,
		// 		like: false,
		// 		imagem:  this.imagem
		// 	};
		// 	const dataJson = JSON.stringify(data);

		// 	const req = await fetch("http://localhost:3000/cadastros", {
		// 		method: "POST",
		// 		headers: { "Content-Type": "application/json"},
		// 		body: dataJson,
		// 	});
		// 	const res = await req.json();

		// 	console.log(res);
		// 	this.msg = "Cadastro realizado com sucesso!";
		// 	//clear message
		// 	setTimeout(() => (this.msg = ""), 3000);
		// 	//limpar campos
		// 	this.nome = "";
		// 	this.cidade = "";
		// 	this.valor = "";
		// 	this.descricao = "";
		// 	this.imagem = "";
		// },
		// emits: ["newQuarto"],
		// data: () => {
		// 	return {
		// 	title: "",
		// 	}
		// },	
	methods: {
		async addNewQuarto() {
			const campos = {nome: this.nome, valor: this.valor, cidade: this.cidade, description: this.description}
			this.loading = true
			await QuartosApi.addNewQuarto(campos) 
			// this.appStore.showSnackbar(`Novo quarto adicionada #${campos}`)
			this.getQuartos()
			this.loading = false
			console.log("oi")
		},
	}
}
</script>
