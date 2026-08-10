<template>
  <div>
    <h1>Edit your username/stats</h1>
    <h3>
      Your account will remain the same, and your score will also remain the
      same
    </h3>
    <h3>Enter a new username of at least 3 characters</h3>
    <input v-model="userName" placeholder="UserName" />
    <br />

    <br />
    <button
      class="btn btn-warning"
      @click.prevent="updateUserName($auth.user.email, userName)"
      :disabled="
        userName.length < 3 || processing || takenUserName || awaitingCheck
      "
    >
      Update UserName
    </button>
    <br />
    <br />
    <button
      class="btn btn-danger"
      @click.prevent="deleteUserStats($auth.user.email)"
      :disabled="processing"
    >
      Delete all stats
    </button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "EditUserName",
  data() {
    return {
      processing: false,
      userName: "",
      takenUserName: false,
      awaitingCheck: false,
    };
  },
  watch: {
    userName:function (val) {
      if (val.length >= 3) {
        this.checkUsername(val);
      }
    }
  },
  mounted() {},
  methods: {
    updateUserName(email, userName) {
      this.processing = true;
      axios
        .put("/api/users/" + email, {
          user_name: userName,
        })
        .then(() => {
          this.checkUsername(userName);
          alert("Username succesfully updated");
          this.processing = false;
        })
        .catch((error) => {
          this.processing = false;
          alert(error);
        });
    },
    checkUsername(userName) {
      this.processing = true;
      axios
        .get("/api/users/check_username/" + userName)
        .then(() => {
          this.processing = false;
          this.takenUserName = false;
          return true;
        })
        .catch(() => {
          this.processing = false;
          this.takenUserName = true;
          return false;
        });
    },
    deleteUserStats(email) {
      if (
        confirm(
          "Are you sure you want to delete all stats for " +
            email +
            "? This will navigate you to the dashboard where you will have to set a new username and your scores wil be reset to zero"
        )
      ) {
        this.processing = true;
        axios
          .delete("/api/users/" + email)
          .then(() => {
            this.processing = false;
            this.$router.push("/dashboard");
          })
          .catch((error) => {
            alert(error);
          });
      }
    },
  },
};
</script>

