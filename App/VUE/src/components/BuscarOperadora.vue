<template>
  <div>
    <h2>Buscar Operadoras</h2>
    <input v-model="query" @keyup.enter="buscarOperadora" />
    <button @click="buscarOperadora">Buscar</button>
    <div v-if="error">{{ error }}</div>
    <ul>
      <li v-for="operadora in resultados" :key="operadora.Nome">
        {{ operadora.Nome }} - {{ operadora.Codigo }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      query: '',
      resultados: [],
      error: ''
    };
  },
  methods: {
    buscarOperadora() {
      if (this.query === '') {
        this.error = 'Erro: Digite algo';
        return;
      }
      axios.get('http://127.0.0.1:5000/buscar?q=' + this.query).then((response) => {
        this.resultados = response.data;
        this.error = '';
      }).catch(() => {
        this.error = 'Erro ao buscar';
      });
    }
  }
};
</script>

<style scoped>
div {
  margin: auto;
  text-align: left;
}
input {
  width: 100%;
}
.error {
  color: red;
}
</style>
