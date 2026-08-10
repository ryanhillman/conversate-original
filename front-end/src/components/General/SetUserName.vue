<template>
  <div>
    <h1>Set your User Name!</h1>
    <h3>
      Your username will be used as your unique identifieer for games, friends,
      and Mastery.
    </h3>
    <h3>
      Your email is: {{ $auth.user.email }}, please enter a username to use for
      your account of at least 3 characters
    </h3>
    <input v-model="userName" placeholder="UserName" />
    <br />
    <br />
    <button
      class="btn btn-success"
      @click.prevent="updateUserName($auth.user.email, userName)"
      :disabled="userName.length < 3"
    >
      Update UserName
    </button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Mastery",
  data() {
    return {
      userName: "",
    };
  },
  mounted() {},
  methods: {
    updateUserName(email, userName) {
      axios
        .post("/api/users", {
          email: email,
          user_name: userName,
        })
        .then(() => {
          this.$router.push("/profile");
        }).catch((error) => {
          alert(error);
        });
    },
  },
};
</script>

