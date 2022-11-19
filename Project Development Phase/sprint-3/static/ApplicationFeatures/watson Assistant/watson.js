window.watsonAssistantChatOptions = {
    integrationID: "a6d7e889-59ed-46da-8168-775bffd4611e", // The ID of this integration.
    region: "us-east", // The region your integration is hosted in.
    serviceInstanceID: "97212d7f-a694-4baf-a9a3-40807857702a", // The ID of your service instance.
    onLoad: function(instance) { instance.render(); }
  };
  setTimeout(function(){
    const t=document.createElement('script');
    t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js";
    document.head.appendChild(t);
  });