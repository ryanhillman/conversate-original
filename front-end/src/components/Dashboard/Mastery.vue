<template>
  <div v-if="user">
    <div class="card-style">
      <h1><i>Mastery</i></h1>
      <h3>
        You have a mastery of {{ (user.score / 9) * 100 }}% ({{ user.score }}
        out of 9)
        <br />
      </h3>
    </div>
    <div class="card" style="width: 18rem">
        <div class="card-body">
          <h5 class="card-title">
            Complete more lessons to improve your mastery!
          </h5>
          <a href="/lesson" class="btn btn-primary">Lessons</a>
        </div>
      </div>
  </div>
  <div v-else>
      <SetUserName />
    </div>
</template>

<script>
import axios from "axios";
import SetUserName from "../General/SetUserName.vue";
export default {
  name: "Mastery",
  components: {
    SetUserName,
  },
  data() {
    return {
      users: null,
      err: null,
      user: null,
      processing: false,
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
          this.processing = false;
          this.user = response.data;
        })
        .catch(() => {
          this.processing = false;
        });
    },
    updateUsers() {
      axios.get("/api/users").then((response) => {
        this.users = response.data;
      });
    },
  },
};
</script>
<style lang="scss" scoped>
.card-style {
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 1rem;
  margin: 2rem auto;
  max-width: 40rem;
  color: white;
  background-color: #152f68;
  font-family: "Roboto", sans-serif;
  font-weight: 400;
  text-align: center;
  align-content: center;
}
.card{
  margin-left: auto;
  margin-right: auto;
  text-align: center;
}
</style>