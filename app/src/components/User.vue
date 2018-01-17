<template>
  <div id="users">
    <div v-for="(user, i) in users" v-bind:key="i">
      <div class="field has-addons">
        <div class="control">
          <input class="input" type="text" v-model="user.nome">
        </div>
        <div class="control">
          <button class="button is-warning" @click="updateUser(user)">Alterar</button>
        </div>
        <div class="control">
          <button class="button is-danger" @click="deleteUser(user, i)">Excluir</button>
        </div>
      </div>

    </div>
    <div class="field has-addons">
      <div class="control">
        <input type="text" class="input" placeholder="João Augusto" v-model="newUser">
      </div>
      <div class="control">
        <button class="button is-success" @click="insertUser(newUser)">Inserir</button>
      </div>
    </div>
  </div>

</template>

<script>
import axios from 'axios'
import config from '../config'

export default {
  data: ()=> ({
    users: [],
    newUser: "",
  }),
  created() {
    this.getAllUsers();
  },
  methods: {
    async getAllUsers() {
      try {
        const users = await axios.get(`${config.SERVER_ADDRESS}/${config.ROUTES.USER}`);
        this.users = users.data;
      } catch (error) {
        console.log(error);
      }
    },

    async updateUser(user) {
      const url = `${config.SERVER_ADDRESS}/${config.ROUTES.USER}/${user.id_usuario}`;
      try {
        await axios.put(url, user);
        alert("SALVO");
      } catch (error) {
        console.log("Erro ao salvar.");
      }
    },

    async deleteUser(user, i) {
      const url = `${config.SERVER_ADDRESS}/${config.ROUTES.USER}/${user.id_usuario}`;
      try {
        await axios.delete(url, user);
        this.users.splice(i, 1);
      } catch (error) {
        console.log(error);
      }
    },

    async insertUser(newUser) {
      const url = `${config.SERVER_ADDRESS}/${config.ROUTES.USER}`;
      try {
        const data = await axios.post(url, { nome: newUser });
        const id = data.headers['last-inserted-id'];
        this.users.push({ nome: newUser, id_usuario: id });
      } catch (error) {
        console.log(error);
      }
    },

  }
}
</script>

<style lang="sass" scoped>
@import "~bulma/sass/utilities/_all";
@import "~bulma/sass/elements/form";
@import "~bulma/sass/elements/button";

.control { padding-top: 10px; padding-bottom: 10px; }
.input { width: 300px; }
.button { height: 100%; }
</style>
