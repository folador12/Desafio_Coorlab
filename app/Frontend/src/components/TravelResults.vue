<template>
  <div class="travel-results">
    <h3 class="results-title">
      Estas são as melhores alternativas de viagem para a data selecionada
    </h3>

    <div class="result-card" v-if="travelOptions && travelOptions.fastest">
      <div class="result-icon">
        <span class="material-icons">volunteer_activism</span>
      </div>
      <div class="result-details">
        <h2 class="result-name">{{ travelOptions.fastest.name }}</h2>
        <div class="result-duration">
          Tempo estimado: {{ travelOptions.fastest.duration }}h
        </div>
        <div class="result-seat">Leito: {{ travelOptions.fastest.bed }}</div>
      </div>
      <div class="result-price">
        Preço: R$ {{ travelOptions.fastest.price_confort }}
      </div>
    </div>

    <div class="result-card" v-if="travelOptions && travelOptions.cheapest">
      <div class="result-icon">
        <span class="material-icons">update</span>
      </div>
      <div class="result-details">
        <h2 class="result-name">{{ travelOptions.cheapest.name }}</h2>
        <div class="result-duration">
          Tempo estimado: {{ travelOptions.cheapest.duration }}h
        </div>
        <div class="result-seat">
          Poltrona: {{ travelOptions.cheapest.seat }}
        </div>
      </div>
      <div class="result-price">
        Preço: R$ {{ travelOptions.cheapest.price_econ }}
      </div>
    </div>

    <button @click="clearResults" class="clear-results-btn">Limpar</button>
  </div>
</template>

<script>
export default {
  name: "TravelResults",
  props: {
    travelOptions: Object,
  },
  methods: {
    clearResults() {
      this.$emit("clear-results");
    },
  },
};
</script>

<style scoped>
.travel-results {
  margin: 1em 0;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 1em;
}

.results-title {
  margin-bottom: 1em;
  color: #fff;
}

.material-icons {
  font-size: 6rem;
  color: #fff;
}

.result-card {
  display: flex;
  align-items: center;
  padding: 1em;
  background-color: #848484;
  border-radius: 10px;
  margin: 10px 0;
}

.result-icon {
  flex-grow: 1;
  display: flex;
  justify-content: center;
}

.result-details {
  flex-grow: 2;
  margin-left: 20px;
}

.result-name,
.result-duration,
.result-seat {
  color: #fff;
}

.result-price {
  font-weight: bold;
  font-size: 1.2em;
  padding: 10px 20px;
  border-radius: 10px;
  background-color: #848484;
  color: #fff;
  margin-left: 20px;
}

.clear-results-btn {
  padding: 10px 20px;
  margin-top: 20px;
  border: none;
  border-radius: 5px;
  background-color: #ffce00;
  color: #000;
  cursor: pointer;
  width: fit-content;
  margin-left: auto;
}
</style>
