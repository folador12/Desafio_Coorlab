<template>
  <div class="search-form">
    <h2><span class="material-icons">volunteer_activism</span> Calcule o valor da viagem</h2>
    <form @submit.prevent="submitSearch">
      <label for="city">Destino</label>
      <select v-model="searchData.city">
        <option value="" disabled>Selecione o destino</option>
        <option value="São Paulo">São Paulo</option>
        <option value="Rio de Janeiro">Rio de Janeiro</option>
        <option value="Belo Horizonte">Belo Horizonte</option>
        <option value="Salvador">Salvador</option>
        <option value="Recife">Recife</option>
        <option value="Campinas">Campinas</option>
        <option value="Curitiba">Curitiba</option>
        <option value="Manaus">Manaus</option>
        <option value="Natal">Natal</option>
      </select>
      <label for="date">Data</label>
      <input type="date" v-model="searchData.date" />
      <button type="submit">Buscar</button>
    </form>
    <error-modal v-if="showErrorModal" @close="showErrorModal = false">
    </error-modal>
  </div>
</template>

<script>
import axios from "axios";
import ErrorModal from "./ErrorModal.vue";

export default {
  name: "SearchForm",
  components: {
    "error-modal": ErrorModal,
  },
  data() {
    return {
      searchData: {
        city: "",
        date: "",
      },
      isLoading: false,
      showErrorModal: false,
    };
  },
  methods: {
    submitSearch() {
      if (!this.searchData.city || !this.searchData.date) {
        this.showErrorModal = true;
      } else {
        this.isLoading = true;
        axios
          .get(`http://localhost:3000/search`, { params: this.searchData })
          .then((response) => {
            this.isLoading = false;
            this.$emit("search-results", response.data);
          })
          .catch((error) => {
            this.isLoading = false;
            console.error(error);
          });
      }
    },
  },
};
</script>

<style>
.search-form {
  background-color: #f8f9fa;
  padding: 20px;
  margin: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.search-form h2 {
  margin-bottom: 30px;
  color: #333;
}

.search-form form {
  display: flex;
  flex-direction: column;
}

.search-form label {
  margin-top: 10px;
  margin-bottom: 5px;
  font-size: 16px;
}

.search-form select,
.search-form input[type="date"] {
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ced4da;
  border-radius: 4px;
}

.search-form button {
  padding: 15px;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: white;
  font-size: 18px;
  cursor: pointer;
  width: 60%;
  margin: 0 auto;
}

.search-form button:hover {
  background-color: #0056b3;
}
</style>
