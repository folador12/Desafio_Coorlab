<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <slot name="header">
              <span class="material-icons modal-close">report</span>
            </slot>
          </div>
          <div class="modal-body">
            <slot name="body">
              Insira os valores para realizar a cotação.
            </slot>
          </div>
          <div class="modal-footer">
            <slot name="footer">
              <button class="modal-default-button" @click="$emit('close')">
                Fechar
              </button>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'ErrorModal'
};
</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-wrapper {
  width: 100%;
  display: flex;
  justify-content: center;
}

.modal-container {
  width: 400px;
  background-color: #fff;
  border-radius: 8px; 
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.2);
  padding: 20px;
}

.modal-header {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}


.modal-body {
  text-align: center;
  padding: 0 20px 20px;
  font-size: 1.5rem;
}

.modal-footer {
  display: flex;
  justify-content: center;
}

.modal-default-button {
  background-color: #03a8b5; 
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px; 
  font-size: 1rem;
  margin-top: 20px;
  cursor: pointer;
  outline: none;
  width: 60%; 
  box-sizing: border-box; 
}

.modal-default-button:hover {
  background-color: #0056b3; 
}


.material-icons {
  font-size: 80px;
  color: #03aebc;
  vertical-align: middle;
  margin-right: 5px;
  padding-bottom: 20px;
}


.modal-enter-active, .modal-leave-active {
  transition: opacity 0.5s;
}

.modal-enter, .modal-leave-to {
  opacity: 0;
}

</style>
