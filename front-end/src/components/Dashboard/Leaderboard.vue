<template>
  <div>
    <h1>Leaderboards</h1>
    <div v-if="user">
      You: {{ user.user_name }}
      <ul>
        <li v-for="user in users" :key="user.id">
          score: {{ user.score }}, username: {{user.user_name}}, email: {{user.email}}, id: {{user.id}}
        </li>
      </ul>
    </div>
    <div v-else>
      <SetUserName />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import SetUserName from "../General/SetUserName.vue"
export default {
  name: "Leaderboard",
  components: {
    SetUserName
  },
  data() {
    return {
      users: null,
      err: null,
      user: null,
      processing: false
    };
  },
  mounted() {
    this.updateUser(this.$auth.user.email);
    this.updateUsers();
  },
  methods: {
    updateUser(email) {
      this.processing = true;
      axios
        .get("/api/users/" + email)
        .then((response) => {
          this.processing = false
          this.user = response.data;
        }).catch(() => {
          this.processing = false;
        });
    },
    updateUsers() {
      axios
        .get("/api/users")
        .then((response) => {
          this.users = response.data;
        });
    },
  },
};
</script>

