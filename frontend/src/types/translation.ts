export interface TranslationRequest {
  text: string;
  target_language: string;
}

export interface TranslationResponse {
  translation: string;
} 