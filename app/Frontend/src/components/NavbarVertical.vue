<template>
  <aside class="navbar">
    <img src="../assets/logo.png" alt="CB Viagens Logo" class="logo" />
    <nav>
      <ul>
        <li class="active"> <span class="material-icons">calculate</span> Calculadora de Viagem</li>
      </ul>
    </nav>
    <slot class="content"></slot>
  </aside>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style>
.navbar {
  width: 300px;
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
  background: #2C3E50;
  color: white;
}

.navbar ul {
  list-style: none;
  padding: 0;
}

.navbar li {
  padding: 15px 20px;
  text-align: center;
}

.navbar a {
  color: white;
  text-decoration: none;
}

.logo {
  width: 100%;
  margin: 20px 0;
}

.active {
  background: #444;
}

.material-icons {
  margin-top: 5px;
  margin-right: 5px;
}

</style>