import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export default class HomeComponent {
  isChatbotOpen = false; 
  chatbotMessages: { sender: string; message: string; isUser: boolean }[] = [];

  toggleChatbot() {
    this.isChatbotOpen = !this.isChatbotOpen;
  }

  sendMessage(event: KeyboardEvent, inputElement: HTMLInputElement) {
    if (event.key === 'Enter' && inputElement.value.trim() !== '') {
      const userMessage = inputElement.value.trim();
      inputElement.value = '';

      this.chatbotMessages.push({ sender: 'user', message: userMessage, isUser: true });

      setTimeout(() => {
        this.handleBotResponse(userMessage);
      }, 1000);
    }
  }

  handleBotResponse(message: string) {
    const lowerMessage = message.toLowerCase();
    let botResponse = 'Gracias por tu mensaje. ¿Necesitas ayuda con algo más?';

    if (lowerMessage.includes('crear cuenta')) {
      botResponse = 'Para crear una cuenta en Prestabank, sigue estos pasos:<br>1. Visita nuestra página de registro.<br>2. Completa el formulario con tus datos.<br>3. Verifica tu identidad.<br>4. ¡Listo! Tu cuenta será activada en minutos.';
    } else if (lowerMessage.includes('más información')) {
      botResponse = 'Un asesor se contactará contigo en breve para brindarte más información. ¡Gracias!';
    } else if (lowerMessage.includes('beneficios')) {
      botResponse = '¡Ser cliente de Prestabank tiene grandes beneficios!<br>✨ Acumula millas por cada compra y canjéalas por viajes gratuitos.<br>💳 Accede a tarjetas de crédito con tasas preferenciales.<br>📈 Invierte con nosotros y obtén rendimientos exclusivos.<br>📱 Gestiona todo desde nuestra app segura y fácil de usar.';
    }

    this.chatbotMessages.push({ sender: 'bot', message: botResponse, isUser: false });
  }
}
