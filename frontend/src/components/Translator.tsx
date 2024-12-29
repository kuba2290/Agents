import React, { useState } from 'react';
import {
    Box,
    Button,
    Container,
    FormControl,
    FormLabel,
    Input,
    Select as ChakraSelect,
    Text,
    VStack,
    useToast,
    Flex,
    } from "@chakra-ui/react";
import { translateText } from '../services/api';

// Move interfaces to types file
interface TranslationRequest {
  text: string;
  target_language: string;
}

interface TranslationResponse {
  translation: string;
}

interface Translation {
  original: string;
  translated: string;
  targetLanguage: string;
  timestamp: Date;
}

const LANGUAGES = [
  'English',
  'Spanish',
  'French',
  'German',
  'Italian',
  'Portuguese',
  'Russian',
  'Japanese',
  'Korean',
  'Chinese',
] as const;

type Language = typeof LANGUAGES[number];

export const Translator: React.FC = () => {
  const [text, setText] = useState('');
  const [targetLanguage, setTargetLanguage] = useState<Language>('English');
  const [translations, setTranslations] = useState<Translation[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const toast = useToast();

  const handleTranslate = async () => {
    if (!text.trim()) {
      toast({
        title: 'Error',
        description: 'Please enter some text to translate',
        status: 'error',
        duration: 3000,
        isClosable: true,
      });
      return;
    }

    setIsLoading(true);
    try {
      const response = await translateText({
        text,
        target_language: targetLanguage,
      });

      const newTranslation: Translation = {
        original: text,
        translated: response.translation,
        targetLanguage,
        timestamp: new Date(),
      };

      setTranslations(prev => [newTranslation, ...prev]);
      setText('');
    } catch (error) {
      toast({
        title: 'Translation Error',
        description: error instanceof Error ? error.message : 'Failed to translate text',
        status: 'error',
        duration: 3000,
        isClosable: true,
      });
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleTranslate();
    }
  };

  return (
    <Container maxW="container.lg" py={8}>
      <VStack spacing={6}>
        <Text fontSize="3xl" fontWeight="bold" color="blue.600">
          Pidgin English Translator
        </Text>

        <Flex width="full" gap={4}>
          <FormControl flex={3}>
            <FormLabel>Enter Pidgin English Text</FormLabel>
            <Input
              value={text}
              onChange={(e) => setText(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Enter text to translate..."
              size="lg"
            />
          </FormControl>

          <FormControl flex={1}>
            <FormLabel>Target Language</FormLabel>
            <ChakraSelect
              value={targetLanguage}
              onChange={(e: React.ChangeEvent<HTMLSelectElement>) => setTargetLanguage(e.target.value as Language)}
              size="lg"
            >
              {LANGUAGES.map((lang) => (
                <option key={lang} value={lang}>
                  {lang}
                </option>
              ))}
            </ChakraSelect>
          </FormControl>
        </Flex>

        <Button
          colorScheme="blue"
          onClick={handleTranslate}
          isLoading={isLoading}
          size="lg"
          width="full"
        >
          Translate
        </Button>

        <VStack spacing={4} width="full" align="stretch">
          {translations.map((item, index) => (
            <Box
              key={index}
              p={4}
              bg="white"
              shadow="md"
              borderRadius="lg"
              borderWidth="1px"
            >
              <Text color="gray.500" fontSize="sm">
                {item.timestamp.toLocaleTimeString()}
              </Text>
              <Text fontWeight="bold" mt={2}>
                Original (Pidgin English): {item.original}
              </Text>
              <Text mt={2}>
                Translated ({item.targetLanguage}): {item.translated}
              </Text>
            </Box>
          ))}
        </VStack>
      </VStack>
    </Container>
  );
};