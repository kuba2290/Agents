import axios from 'axios';
import { TranslationRequest, TranslationResponse } from '../types/translation';

const API_URL = 'http://localhost:8000';

export const translateText = async (request: TranslationRequest): Promise<TranslationResponse> => {
  const response = await axios.post<TranslationResponse>(`${API_URL}/translate`, request);
  return response.data;
};