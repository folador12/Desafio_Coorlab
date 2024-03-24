<template>
  <div id="app">
    <NavbarTop />
    <div class="container-fluid">
      <div class="row">
        <NavbarVertical />
        <main>
          <div class="main-title">
            <h1>
              <span class="material-icons"> local_shipping </span>
              Calculadora de Viagem
            </h1>
          </div>
          <div class="main-body">
            <div class="results-container">
              <SearchForm @search-results="updateResults" />
              <TravelResults
                v-if="results"
                :travelOptions="results"
                @clear-results="clearResults"
              />
              <div v-if="!results" class="no-data">Nenhum dado selecionado.</div>
            </div>
          </div>
        </main>
      </div>
    </div>
  </div>
</template>

<script>
import NavbarTop from "./components/NavbarTop.vue";
import NavbarVertical from "./components/NavbarVertical.vue";
import SearchForm from "./components/SearchForm.vue";
import TravelResults from "./components/TravelResults.vue";

export default {
  components: {
    NavbarTop,
    NavbarVertical,
    SearchForm,
    TravelResults,
  },
  data() {
    return {
      results: null,
    };
  },
  methods: {
    updateResults(data) {
      this.results = data;
    },
    clearResults() {
      this.results = null;
    },
  },
};
</script>

<style>
.navbar-vertical {
  background-color: #f8f9fa;
  height: 100vh;
}

.container-fluid {
  max-width: 100%; 
}


.main-title {
  background-color: #000000;
  color: #ffffff;
  padding: 20px 10px;
  text-align: center;
  width: 100%;
}

.main-body {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start; 
  background-color: #ffffff;
  padding: 30px;
  gap: 20px;
  width: 100%;
  overflow: hidden; 
}

.no-data {
  margin: auto;
  width: 60%; 
  height: 100%; 
  text-align: center;
}

.results-container {
  display: flex;
  justify-content: space-between; 
  width: 100%;
}


.search-form {
  margin-right: 20px;
  max-width: 40%;
}

.travel-results {
  max-width: 60%; 
}


.search-form, .travel-results {
  
  flex: 1; 
}

main {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  max-width: 1500px; 
  margin-top: 100px; 
  margin-left: 330px; 
  border: 1px solid #ccc;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

</style>
