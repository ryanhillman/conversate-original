<template>
    <div>
    <h1> Question API </h1>
    </table>
        </div>
        <td>Question</td>
    </tr>
    </div>
</template>
<script>
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
axios.use(VueAxios, axios);
export default {
    name: "questions"
    mounted() {
        axios.get(https://github.com/hendurhance/quizapp).then((resp)=>{
            this.list = resp.data.data;
            console.warn(resp.data.data);
        })
    }
}
</script>