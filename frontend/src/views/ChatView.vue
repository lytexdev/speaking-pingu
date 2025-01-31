<template>
    <div class="chat-container">
        <Logo title="Speaking-Pingu AI" />

        <div class="chat-box">
            <div class="message bot">
                <span>Hello! How can I assist you?</span>
            </div>
            <div class="message user">
                <span>Hey, could you tell me something about raw milk?</span>
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
import { ref, onMounted } from "vue"
import Logo from "@/components/Logo.vue"

const userInput = ref("")

const sendMessage = () => {
    if (!userInput.value.trim()) return
    alert("Message Sent: " + userInput.value)
    userInput.value = ""
}
</script>
