<template>
  <div id="users">
    <div v-for="(user, i) in users" v-bind:key="i">
      <div class="field has-addons">
        <div class="control">
          <input class="input" type="text" v-model="user.nome">
        </div>
        <div class="control">
          <button class="button is-info" v-on:click="updateUser(user)">Alterar</button>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import axios from 'axios'
import config from '../config'

export default {
  data: ()=> ({
    users: []
  }),
  created() {
    this.getAllUsers();
  },
  methods: {
    async getAllUsers() {
      try {
        let users = await axios.get(config.SERVER_ADDRESS + config.ROUTES.USER);
        this.users = users.data;
      } catch (error) {
        console.log(error);
      }
    },

    async updateUser(user) {
      try {
        await axios.put(config.SERVER_ADDRESS + `/user/${user.id_usuario}`, user);
        alert("SALVO");
      } catch (error) {
        console.log("Erro ao salvar.");
      }
    }
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
