<template>
    <div class="chat-container">
        <Logo title="Speaking-Pingu AI" />

        <div class="chat-box">
            <div v-for="(message, index) in messages" :key="index" :class="['message', message.role]">
                <span>{{ message.text }}</span>
            </div>
        </div>

        <div class="chat-input-container flex">
            <input v-model="userInput" placeholder="Type a message..." class="input-field"
                @keypress.enter="sendMessage" />
            <button @click="sendMessage" class="btn">Send</button>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import Logo from "@/components/Logo.vue";
import axios from "axios";

const userInput = ref("");
const messages = ref([
    { text: "Hello! How can I assist you?", role: "bot" }
]);

const sendMessage = async () => {
    if (!userInput.value.trim()) return;

    const userMessage = { text: userInput.value, role: "user" };
    messages.value.push(userMessage);

    const prompt = userInput.value;
    userInput.value = "";

    try {
        const response = await axios.post("/api/chat", { prompt });
        const botMessage = { text: response.data.response, role: "bot" };
        messages.value.push(botMessage);
    } catch (error) {
        messages.value.push({ text: "Error fetching response!", role: "error" });
    }
};
</script>
