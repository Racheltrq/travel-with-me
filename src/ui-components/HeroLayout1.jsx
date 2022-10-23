/***************************************************************************
 * The contents of this file were generated with Amplify Studio.           *
 * Please refrain from making any modifications to this file.              *
 * Any changes to this file will be overwritten when running amplify pull. *
 **************************************************************************/

/* eslint-disable */
import React from "react";
import {
  getOverrideProps,
  getOverridesFromVariants,
  mergeVariantsAndOverrides,
  useNavigateAction,
} from "@aws-amplify/ui-react/internal";
import { User, Agent } from "../models";
import { Button, Flex, Image, Text } from "@aws-amplify/ui-react";
import travelLogo from "../static/travelLogo.jpg"

export default function HeroLayout1(props) {
  const { overrides: overridesProp, ...rest } = props;
  const variants = [
    {
      overrides: {
        TravelWithMe: {},
        "The place for your to connect tourguide": {},
        "There\u2019s no better way to feel the heartbeat of a city than discovering it with a knowledgeable local by your side who has similar interests to yours. Whether travelers want the focus of your visit to be on art, food, nightlife, sightseeing, or culture, they can customize a city tour with a Travel with Me local whatever their next destination.":
          {},
        Message: {},
        Button: {},
        HeroMessage: {},
        Left: {},
        image: { src: { travelLogo }},
        Right: {},
        HeroLayout1: {},
      },
      variantValues: { mode: "Light" },
    },
    {
      overrides: {
        TravelWithMe: { color: "rgba(255,255,255,1)" },
        "The place for your to connect tourguide": {
          color: "rgba(255,255,255,1)",
        },
        "There\u2019s no better way to feel the heartbeat of a city than discovering it with a knowledgeable local by your side who has similar interests to yours. Whether travelers want the focus of your visit to be on art, food, nightlife, sightseeing, or culture, they can customize a city tour with a Travel with Me local whatever their next destination.":
          { color: "rgba(255,255,255,1)" },
        Message: {},
        Button: {},
        HeroMessage: {},
        Left: { backgroundColor: "rgba(0,0,0,1)" },
        image: { alignSelf: "stretch", objectFit: "cover", src: { travelLogo }},
        HeroLayout1: {},
      },
      variantValues: { mode: "Dark" },
    },
  ];
  const overrides = mergeVariantsAndOverrides(
    getOverridesFromVariants(variants, props),
    overridesProp || {}
  );
  const buttonOnClick = useNavigateAction({ type: "url", url: "feed" });
  const imageOnClick = useNavigateAction({ type: "url", url: "" });
  return (
    <Flex
      gap="0"
      width="1700px"
      height="500px"
      justifyContent="center"
      alignItems="center"
      position="relative"
      padding="0px 0px 0px 0px"
      display="flex"
      {...rest}
      {...getOverrideProps(overrides, "HeroLayout1")}
    >
      <Flex
        gap="10px"
        direction="column"
        width="100%"
        justifyContent="center"
        alignItems="center"
        grow="1"
        alignSelf="stretch"
        overflow="hidden"
        position="relative"
        padding="120px 120px 120px 120px"
        backgroundColor="rgba(255,255,255,1)"
        display="flex"
        {...getOverrideProps(overrides, "Left")}
      >
        <Flex
          gap="24px"
          direction="column"
          justifyContent="center"
          alignItems="center"
          shrink="0"
          alignSelf="stretch"
          objectFit="cover"
          position="relative"
          padding="0px 0px 0px 0px"
          display="flex"
          {...getOverrideProps(overrides, "HeroMessage")}
        >
          <Text
            fontFamily="Inter"
            fontSize="40px"
            fontWeight="700"
            color="rgba(13,26,38,1)"
            lineHeight="48px"
            textAlign="center"
            display="flex"
            direction="column"
            justifyContent="flex-start"
            shrink="0"
            alignSelf="stretch"
            objectFit="cover"
            position="relative"
            padding="0px 0px 0px 0px"
            whiteSpace="pre-wrap"
            children="Travel With Me"
            {...getOverrideProps(overrides, "Travel With Me")}
          ></Text>
          <Flex
            gap="16px"
            direction="column"
            justifyContent="center"
            alignItems="center"
            shrink="0"
            alignSelf="stretch"
            objectFit="cover"
            position="relative"
            padding="0px 0px 0px 0px"
            display="flex"
            {...getOverrideProps(overrides, "Message")}
          >
            <Text
              fontFamily="Inter"
              fontSize="24px"
              fontWeight="400"
              color="rgba(13,26,38,1)"
              lineHeight="30px"
              textAlign="center"
              display="flex"
              direction="column"
              justifyContent="flex-start"
              shrink="0"
              alignSelf="stretch"
              objectFit="cover"
              position="relative"
              padding="0px 0px 0px 0px"
              whiteSpace="pre-wrap"
              children="The place for your to connect with your tour guide"
              {...getOverrideProps(
                overrides,
                "The place for your to connect with your tour guide"
              )}
            ></Text>
            <Text
              fontFamily="Inter"
              fontSize="16px"
              fontWeight="400"
              color="rgba(13,26,38,1)"
              lineHeight="24px"
              textAlign="justify"
              display="flex"
              direction="column"
              justifyContent="flex-start"
              letterSpacing="0.01px"
              shrink="0"
              alignSelf="stretch"
              objectFit="cover"
              position="relative"
              padding="0px 0px 0px 0px"
              whiteSpace="pre-wrap"
              children="There’s no better way to feel the heartbeat of a city than discovering it with a knowledgeable local by your side who has similar interests to yours. Whether travelers want the focus of your visit to be on art, food, nightlife, sightseeing, or culture, they can customize a city tour with a Travel with Me local whatever their next destination."
              {...getOverrideProps(
                overrides,
                "There\u2019s no better way to feel the heartbeat of a city than discovering it with a knowledgeable local by your side who has similar interests to yours. Whether travelers want the focus of your visit to be on art, food, nightlife, sightseeing, or culture, they can customize a city tour with a Travel with Me local whatever their next destination."
              )}
            ></Text>
          </Flex>
          <Button
            display="flex"
            gap="0"
            width="fit-content"
            justifyContent="center"
            alignItems="center"
            shrink="0"
            position="relative"
            size="large"
            isDisabled={false}
            variation="primary"
            children="Start to Search"
            onClick={() => {
              buttonOnClick();
            }}
            {...getOverrideProps(overrides, "Button")}
          ></Button>
        </Flex>
      </Flex>
      <Flex
        gap="10px"
        direction="column"
        width="100%"
        justifyContent="center"
        alignItems="center"
        grow="1"
        alignSelf="stretch"
        overflow="hidden"
        position="relative"
        padding="0px 0px 0px 0px"
        display="flex"
        {...getOverrideProps(overrides, "Right")}
      >
        <Image
          src = {travelLogo}
          width="720px"
          height="500px"
          grow="1"
          position="relative"
          padding="0px 0px 0px 0px"
          display="flex"
          onClick={() => {
            imageOnClick();
          }}
          {...getOverrideProps(overrides, "image")}
        ></Image>
      </Flex>
    </Flex>
  );
}
