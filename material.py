import pygame


class image:
    #####################
    pixel_per_block = 64
    fix = pixel_per_block / 64
    #####################

    playerImg = pygame.transform.scale(pygame.image.load(
        "images/player.png"), (int(64 * fix), int(64 * fix)))
    slimeImg = pygame.transform.scale(pygame.image.load(
        "images/slime.png"), (int(32 * fix), int(32 * fix)))
    bossImg = pygame.transform.scale(pygame.image.load(
        "images/boss.png"), (int(64 * fix), int(64 * fix)))
    aimImg = pygame.transform.scale(pygame.image.load(
        "images/aim.png"), (int(32 * fix), int(32 * fix)))
    toolBarImg = pygame.transform.scale(
        pygame.image.load("images/toolBar.png"), (int(344 * fix), int(64 * fix)))
    selectedBarImg = pygame.transform.scale(pygame.image.load(
        "images/selectedBar.png"), (int(72 * fix), int(64 * fix)))
    speedupBoostImg = pygame.transform.scale(
        pygame.image.load("images/speedupBoost.png"), (int(58 * fix), int(58 * fix)))
    wand_1_Img = pygame.transform.scale(pygame.image.load(
        "images/wand_1.png"), (int(48 * fix), int(48 * fix)))

    wand_2_Img = pygame.transform.scale(
        pygame.image.load("images/wand_2.png"), (int(48 * fix), int(48 * fix)))

    fireball_sprites = []

    fireball_sprites.append(pygame.transform.scale(
        pygame.image.load("images/fireball/FB001.png"), (int(64 * fix), int(64 * fix))))
    fireball_sprites.append(pygame.transform.scale(
        pygame.image.load("images/fireball/FB002.png"), (int(64 * fix), int(64 * fix))))
    fireball_sprites.append(pygame.transform.scale(
        pygame.image.load("images/fireball/FB003.png"), (int(64 * fix), int(64 * fix))))
    fireball_sprites.append(pygame.transform.scale(
        pygame.image.load("images/fireball/FB004.png"), (int(64 * fix), int(64 * fix))))
    fireball_sprites.append(pygame.transform.scale(
        pygame.image.load("images/fireball/FB005.png"), (int(64 * fix), int(64 * fix))))

    explosionImg1 = pygame.transform.scale(
        pygame.image.load("images/fireball/B500-2.png"), (int(64 * fix), int(64 * fix)))
    explosionImg2 = pygame.transform.scale(
        pygame.image.load("images/fireball/B500-3.png"), (int(64 * fix), int(64 * fix)))
    explosionImg3 = pygame.transform.scale(
        pygame.image.load("images/fireball/B500-4.png"), (int(64 * fix), int(64 * fix)))

    boostEffectImg = pygame.transform.scale(
        pygame.image.load("images/boostEffect.png"), (int(48 * fix), int(48 * fix)))

    bossImg = pygame.transform.scale(bossImg, (int(128 * fix), int(128 * fix)))

    endGame_sprites = []
    endGame_sprites.append(pygame.transform.scale(
        pygame.image.load("images/scene/endTitle/endGame_1.png"), (int(800 * fix), int(400 * fix))))
    endGame_sprites.append(pygame.transform.scale(
        pygame.image.load("images/scene/endTitle/endGame_2.png"), (int(800 * fix), int(400 * fix))))

    mysteryChestInfoImg = pygame.transform.scale(pygame.image.load(
        "images/scene/shop/mysteryChestInfo.png"), (int(800 * fix), int(400 * fix)))
    healthPotionChestInfoImg = pygame.transform.scale(
        pygame.image.load("images/scene/shop/healthPotionChestInfo.png"), (int(800 * fix), int(400 * fix)))
    manaPotionChestInfoImg = pygame.transform.scale(
        pygame.image.load("images/scene/shop/manaPotionChestInfo.png"), (int(800 * fix), int(400 * fix)))

    buyConfirm_sprites = []
    if True:
        buyConfirm_sprites.append(pygame.transform.scale(
            pygame.image.load("images/scene/shop/confirmBuy/confirmBuy_1.png"), (int(400 * fix), int(160 * fix))))
        buyConfirm_sprites.append(pygame.transform.scale(
            pygame.image.load("images/scene/shop/confirmBuy/confirmBuy_2.png"), (int(400 * fix), int(160 * fix))))
        buyConfirm_sprites.append(pygame.transform.scale(
            pygame.image.load("images/scene/shop/confirmBuy/confirmBuy_3.png"), (int(400 * fix), int(160 * fix))))
        buyConfirm_sprites.append(pygame.transform.scale(
            pygame.image.load("images/scene/shop/confirmBuy/confirmBuy_4.png"), (int(400 * fix), int(160 * fix))))

    teleportConfirm_sprites = []
    if True:
        teleportConfirm_sprites.append(pygame.transform.scale(
            pygame.image.load("images/scene/teleportConfirm/teleportConfirm_1.png"), (int(400 * fix), int(160 * fix))))
        teleportConfirm_sprites.append(pygame.transform.scale(
            pygame.image.load("images/scene/teleportConfirm/teleportConfirm_2.png"), (int(400 * fix), int(160 * fix))))
        teleportConfirm_sprites.append(pygame.transform.scale(
            pygame.image.load("images/scene/teleportConfirm/teleportConfirm_3.png"), (int(400 * fix), int(160 * fix))))
        teleportConfirm_sprites.append(pygame.transform.scale(
            pygame.image.load("images/scene/teleportConfirm/teleportConfirm_4.png"), (int(400 * fix), int(160 * fix))))

    woodenChest_sprites = [pygame.transform.scale(pygame.image.load("images/treasures/woodenChest_locked.png"), (int(64 * fix), int(64 * fix))),
                           pygame.transform.scale(pygame.image.load("images/treasures/woodenChest_opened.png"), (int(64 * fix), int(64 * fix)))]
    silverChest_sprites = [pygame.transform.scale(pygame.image.load("images/treasures/silverChest_locked.png"), (int(64 * fix), int(64 * fix))),
                           pygame.transform.scale(pygame.image.load("images/treasures/silverChest_opened.png"), (int(64 * fix), int(64 * fix)))]
    goldenChest_sprites = [pygame.transform.scale(pygame.image.load("images/treasures/goldenChest_locked.png"), (int(64 * fix), int(64 * fix))),
                           pygame.transform.scale(pygame.image.load("images/treasures/goldenChest_opened.png"), (int(64 * fix), int(64 * fix)))]

    small_woodenChest_sprites = [pygame.transform.scale(pygame.image.load(
        "images/treasures/woodenChest_locked.png"), (int(32 * fix), int(32 * fix))),
        pygame.transform.scale(pygame.image.load("images/treasures/woodenChest_opened.png"), (int(32 * fix), int(32 * fix)))]

    electric_ball_sprites = []

    if True:
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile000.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile001.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile002.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile003.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile004.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile005.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile006.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile007.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile008.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile009.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile010.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile011.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile012.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile013.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile014.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile015.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile016.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile017.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile018.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile019.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile020.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile021.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile022.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile023.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile024.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile025.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile026.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile027.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile028.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile029.png"), (int(64 * fix), int(64 * fix))))
        electric_ball_sprites.append(
            pygame.transform.scale(pygame.image.load("images/electricBall/tile030.png"), (int(64 * fix), int(64 * fix))))

    mana_potion_sprites = []

    if True:
        mana_potion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bluePotion/tile000.png"), (int(32 * fix), int(32 * fix))))
        mana_potion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bluePotion/tile001.png"), (int(32 * fix), int(32 * fix))))
        mana_potion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bluePotion/tile002.png"), (int(32 * fix), int(32 * fix))))
        mana_potion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bluePotion/tile003.png"), (int(32 * fix), int(32 * fix))))
        mana_potion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bluePotion/tile004.png"), (int(32 * fix), int(32 * fix))))
        mana_potion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bluePotion/tile005.png"), (int(32 * fix), int(32 * fix))))
        mana_potion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bluePotion/tile006.png"), (int(32 * fix), int(32 * fix))))
        mana_potion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bluePotion/tile007.png"), (int(32 * fix), int(32 * fix))))

    health_potion_sprites = []

    if True:
        health_potion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/healthPotion/Health Potion 1.png"), (int(32 * fix), int(32 * fix))))
        health_potion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/healthPotion/Health Potion 2.png"), (int(32 * fix), int(32 * fix))))
        health_potion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/healthPotion/Health Potion 3.png"), (int(32 * fix), int(32 * fix))))
        health_potion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/healthPotion/Health Potion 4.png"), (int(32 * fix), int(32 * fix))))
        health_potion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/healthPotion/Health Potion 5.png"), (int(32 * fix), int(32 * fix))))
        health_potion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/healthPotion/Health Potion 6.png"), (int(32 * fix), int(32 * fix))))

    health_potion_org = pygame.transform.scale(pygame.image.load(
        "images/healthPotion/Health Potion 1.png"), (int(16 * fix), int(16 * fix)))
    mana_potionImg_org = pygame.transform.scale(pygame.image.load(
        "images/bluePotion/tile000.png"), (int(16 * fix), int(16 * fix)))

    coinImg = pygame.transform.scale(pygame.image.load(
        "images/coin.png"), (int(16 * fix), int(16 * fix)))
    item_coinImg = pygame.transform.scale(
        pygame.image.load("images/coin.png"), (int(16 * fix), int(16 * fix)))
    heartImg = pygame.transform.scale(pygame.image.load(
        "images/heart.png"), (int(16 * fix), int(16 * fix)))
    broken_heartImg = pygame.transform.scale(pygame.image.load(
        "images/broken_heart.png"), (int(16 * fix), int(16 * fix)))

    coinImg_temp = pygame.transform.scale(
        pygame.image.load("images/coin.png"), (int(16 * fix), int(16 * fix)))
    heartImg_temp = pygame.transform.scale(
        pygame.image.load("images/heart.png"), (int(16 * fix), int(16 * fix)))
    broken_heartImg_temp = pygame.transform.scale(
        pygame.image.load("images/broken_heart.png"), (int(16 * fix), int(16 * fix)))

    # portal parameters
    portal_size = 120

    green_portal_idle_sprites = []
    if True:
        green_portal_idle_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile000.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_idle_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile001.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_idle_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile002.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_idle_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile003.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_idle_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile004.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_idle_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile005.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_idle_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile006.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_idle_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile007.png"), (int(portal_size * fix), int(portal_size * fix))))

    green_portal_open_sprites = []
    if True:
        green_portal_open_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile008.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_open_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile009.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_open_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile010.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_open_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile011.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_open_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile012.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_open_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile013.png"), (int(portal_size * fix), int(portal_size * fix))))

    green_portal_close_sprites = []
    if True:
        green_portal_close_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile013.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_close_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile014.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_close_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile015.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_close_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile016.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_close_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile017.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_close_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile018.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_close_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile019.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_close_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile020.png"), (int(portal_size * fix), int(portal_size * fix))))
        green_portal_close_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/greenPortal/tile021.png"), (int(portal_size * fix), int(portal_size * fix))))

    purple_portal_idle_sprites = []
    if True:
        purple_portal_idle_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile000.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_idle_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile001.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_idle_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile002.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_idle_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile003.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_idle_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile004.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_idle_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile005.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_idle_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile006.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_idle_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile007.png"), (int(portal_size * fix), int(portal_size * fix))))

    purple_portal_open_sprites = []
    if True:
        purple_portal_open_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile008.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_open_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile009.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_open_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile010.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_open_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile011.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_open_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile012.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_open_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile013.png"), (int(portal_size * fix), int(portal_size * fix))))

    purple_portal_close_sprites = []
    if True:
        purple_portal_close_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile013.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_close_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile014.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_close_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile015.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_close_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile016.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_close_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile017.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_close_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile018.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_close_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile019.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_close_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile020.png"), (int(portal_size * fix), int(portal_size * fix))))
        purple_portal_close_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/portals/purplePortal/tile021.png"), (int(portal_size * fix), int(portal_size * fix))))

    spawnEffect_sprites = []
    if True:
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile000.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile001.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile002.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile003.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile004.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile005.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile006.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile007.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile008.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile009.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile010.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile011.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile012.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile013.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile014.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile015.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile016.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile017.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile018.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile019.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile020.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile021.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile022.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile023.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile024.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile025.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile026.png"), (int(96 * fix), int(96 * fix))))
        spawnEffect_sprites.append(
            pygame.transform.scale(pygame.image.load("images/effects/tile027.png"), (int(96 * fix), int(96 * fix))))

    bossExplosion_sprites = []
    if True:
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile000.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile001.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile002.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile003.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile004.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile005.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile006.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile007.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile008.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile009.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile010.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile011.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile012.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile013.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile014.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile015.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile016.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile017.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile018.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile019.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile020.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile021.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile022.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile023.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile024.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile025.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile026.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile027.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile028.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile029.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile030.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile031.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile032.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile033.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile034.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile035.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile036.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile037.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile038.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile039.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile040.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile041.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile042.png"), (int(128 * fix), int(128 * fix))))
        bossExplosion_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossExplosion/tile043.png"), (int(128 * fix), int(128 * fix))))

    bossSpawn_sprites = []
    if True:
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile000.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile001.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile002.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile003.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile004.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile005.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile006.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile007.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile008.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile009.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile010.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile011.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile012.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile013.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile014.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile015.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile016.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile017.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile018.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile019.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile020.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile021.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile022.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile023.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile024.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile025.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile026.png"), (int(192 * fix), int(192 * fix))))
        bossSpawn_sprites.append(pygame.transform.scale(
            pygame.image.load("images/bossSpawn/tile027.png"), (int(192 * fix), int(192 * fix))))

    smoke_sprites = []
    if True:
        smoke_sprites.append(pygame.transform.scale(
            pygame.image.load("images/smoke/tile000.png"), (int(64 * fix), int(64 * fix))))
        smoke_sprites.append(pygame.transform.scale(
            pygame.image.load("images/smoke/tile001.png"), (int(64 * fix), int(64 * fix))))
        smoke_sprites.append(pygame.transform.scale(
            pygame.image.load("images/smoke/tile002.png"), (int(64 * fix), int(64 * fix))))
        smoke_sprites.append(pygame.transform.scale(
            pygame.image.load("images/smoke/tile003.png"), (int(64 * fix), int(64 * fix))))
        smoke_sprites.append(pygame.transform.scale(
            pygame.image.load("images/smoke/tile004.png"), (int(64 * fix), int(64 * fix))))
        smoke_sprites.append(pygame.transform.scale(
            pygame.image.load("images/smoke/tile005.png"), (int(64 * fix), int(64 * fix))))
        smoke_sprites.append(pygame.transform.scale(
            pygame.image.load("images/smoke/tile006.png"), (int(64 * fix), int(64 * fix))))
        smoke_sprites.append(pygame.transform.scale(
            pygame.image.load("images/smoke/tile007.png"), (int(64 * fix), int(64 * fix))))

    spark_sprites = []
    if True:
        spark_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/particle/spark/tile000.png"), (int(16 * fix), int(16 * fix))))
        spark_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/particle/spark/tile001.png"), (int(16 * fix), int(16 * fix))))
        spark_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/particle/spark/tile002.png"), (int(16 * fix), int(16 * fix))))
        spark_sprites.append(pygame.transform.scale(pygame.image.load(
            "images/particle/spark/tile003.png"), (int(16 * fix), int(16 * fix))))

    bar_width = 160 * fix
    bar_height = 27 * fix

    # if statement is just set for folding, it has no other reason
    if True:
        healthBar_sprites = []

        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-100%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-97.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-95%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-92.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-90%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-87.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-85%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-82.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-80%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-77.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-75%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-72.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-70%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-67.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-65%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-62.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-60%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-57.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-55%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-52.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-50%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-47.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-45%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-42.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-40%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-37.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-35%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-32.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-30%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-27.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-25%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-22.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-20%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-17.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-15%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-12.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-10%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-7.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-2.5%.png"))
        healthBar_sprites.append(pygame.image.load(
            "images/healthBar/healthBar-0%.png"))

        manaBar_sprites = []

        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-100%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-97.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-95%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-92.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-90%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-87.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-85%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-82.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-80%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-77.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-75%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-72.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-70%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-67.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-65%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-62.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-60%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-57.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-55%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-52.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-50%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-47.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-45%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-42.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-40%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-37.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-35%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-32.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-30%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-27.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-25%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-22.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-20%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-17.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-15%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-12.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-10%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-7.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-2.5%.png"))
        manaBar_sprites.append(pygame.image.load(
            "images/manaBar/manaBar-0%.png"))

        for iter in range(len(healthBar_sprites)):
            healthBar_sprites[iter] = pygame.transform.scale(
                healthBar_sprites[iter], (int(bar_width), int(bar_height)))

        for iter in range(len(manaBar_sprites)):
            manaBar_sprites[iter] = pygame.transform.scale(
                manaBar_sprites[iter], (int(bar_width), int(bar_height)))

    if True:
        menuBackground = pygame.transform.scale(pygame.image.load(
            "images/scene/menuBackground.jpg"), (int(1920 * fix), int(1202 * fix)))

        gameTitle_sprites = []
        gameTitle_sprites.append(pygame.transform.scale(
            pygame.image.load("images/scene/startTitle/gameTitle2_1.png"), (int(800 * fix), int(400 * fix))))
        gameTitle_sprites.append(pygame.transform.scale(
            pygame.image.load("images/scene/startTitle/gameTitle2_2.png"), (int(800 * fix), int(400 * fix))))

        howToPlay_sprites = []
        howToPlay_sprites.append(pygame.transform.scale(
            pygame.image.load("images/scene/howToPlay/howToPlay_1.png"), (int(800 * fix), int(400 * fix))))
        howToPlay_sprites.append(pygame.transform.scale(
            pygame.image.load("images/scene/howToPlay/howToPlay_2.png"), (int(800 * fix), int(400 * fix))))
        howToPlay_sprites.append(pygame.transform.scale(
            pygame.image.load("images/scene/howToPlay/howToPlay_3.png"), (int(800 * fix), int(400 * fix))))
        howToPlay_sprites.append(pygame.transform.scale(
            pygame.image.load("images/scene/howToPlay/howToPlay_4.png"), (int(800 * fix), int(400 * fix))))
        howToPlay_sprites.append(pygame.transform.scale(
            pygame.image.load("images/scene/howToPlay/howToPlay_5.png"), (int(800 * fix), int(400 * fix))))
        howToPlay_sprites.append(pygame.transform.scale(
            pygame.image.load("images/scene/howToPlay/howToPlay_6.png"), (int(800 * fix), int(400 * fix))))

    wooden_floor_topleft = pygame.transform.scale(
        pygame.image.load("images/scene/floor/wooden/topleft.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    wooden_floor_topright = pygame.transform.scale(
        pygame.image.load("images/scene/floor/wooden/topright.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    wooden_floor_bottomleft = pygame.transform.scale(
        pygame.image.load("images/scene/floor/wooden/bottomleft.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    wooden_floor_bottomright = pygame.transform.scale(
        pygame.image.load("images/scene/floor/wooden/bottomright.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    wooden_floor_bottom = pygame.transform.scale(
        pygame.image.load("images/scene/floor/wooden/bottom.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    wooden_floor_top = pygame.transform.scale(
        pygame.image.load("images/scene/floor/wooden/top.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    wooden_floor_left = pygame.transform.scale(
        pygame.image.load("images/scene/floor/wooden/left.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    wooden_floor_right = pygame.transform.scale(
        pygame.image.load("images/scene/floor/wooden/right.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    wooden_floor_middle = pygame.transform.scale(
        pygame.image.load("images/scene/floor/wooden/middle.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))

    stone_floor_topleft = pygame.transform.scale(
        pygame.image.load("images/scene/floor/stone/topleft.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    stone_floor_topright = pygame.transform.scale(
        pygame.image.load("images/scene/floor/stone/topright.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    stone_floor_bottomleft = pygame.transform.scale(
        pygame.image.load("images/scene/floor/stone/bottomleft.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    stone_floor_bottomright = pygame.transform.scale(
        pygame.image.load("images/scene/floor/stone/bottomright.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    stone_floor_bottom = pygame.transform.scale(
        pygame.image.load("images/scene/floor/stone/bottom.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    stone_floor_top = pygame.transform.scale(
        pygame.image.load("images/scene/floor/stone/top.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    stone_floor_left = pygame.transform.scale(
        pygame.image.load("images/scene/floor/stone/left.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    stone_floor_right = pygame.transform.scale(
        pygame.image.load("images/scene/floor/stone/right.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    stone_floor_middle = pygame.transform.scale(
        pygame.image.load("images/scene/floor/stone/middle.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))

    dungeon_floor_wall = pygame.transform.scale(
        pygame.image.load("images/scene/floor/dungeon/wall.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    dungeon_floor_wall_shadow = pygame.transform.scale(
        pygame.image.load("images/scene/floor/dungeon/wall_shadow.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    dungeon_floor_topleft = pygame.transform.scale(
        pygame.image.load("images/scene/floor/dungeon/topleft.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    dungeon_floor_topright = pygame.transform.scale(
        pygame.image.load("images/scene/floor/dungeon/topright.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    dungeon_floor_top = pygame.transform.scale(
        pygame.image.load("images/scene/floor/dungeon/top.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    dungeon_floor_bottomleft = pygame.transform.scale(
        pygame.image.load("images/scene/floor/dungeon/bottomleft.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    dungeon_floor_bottomright = pygame.transform.scale(
        pygame.image.load("images/scene/floor/dungeon/bottomright.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    dungeon_floor_bottom = pygame.transform.scale(
        pygame.image.load("images/scene/floor/dungeon/bottom.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    dungeon_floor_left = pygame.transform.scale(
        pygame.image.load("images/scene/floor/dungeon/left.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    dungeon_floor_right = pygame.transform.scale(
        pygame.image.load("images/scene/floor/dungeon/right.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))
    dungeon_floor_middle = pygame.transform.scale(
        pygame.image.load("images/scene/floor/dungeon/middle.png"), (int(pixel_per_block * fix), int(pixel_per_block * fix)))

    NPC_size = 60

    tutor = pygame.transform.scale(pygame.image.load(
        "images/scene/tutorial/tutor_1.png"), (int(NPC_size * fix), int(NPC_size * fix)))
    silver_guard = pygame.transform.scale(pygame.image.load(
        "images/NPC/guard/silver.png"), (int(NPC_size * fix), int(NPC_size * fix)))
    golden_guard = pygame.transform.scale(pygame.image.load(
        "images/NPC/guard/silver.png"), (int(NPC_size * fix), int(NPC_size * fix)))

    skeletion_size = 48

    skeleton_idle_sprites = []

    skeleton_idle_sprites.append(pygame.transform.scale(
        pygame.image.load("images/pets/skeleton/idle/tile000.png"), (int(skeletion_size * fix), int(skeletion_size * fix))))
    skeleton_idle_sprites.append(pygame.transform.scale(
        pygame.image.load("images/pets/skeleton/idle/tile001.png"), (int(skeletion_size * fix), int(skeletion_size * fix))))

    skeleton_run_sprites = []

    if True:
        skeleton_run_sprites.append(pygame.transform.scale(
            pygame.image.load("images/pets/skeleton/run/tile000.png"), (int(skeletion_size * fix), int(skeletion_size * fix))))
        skeleton_run_sprites.append(pygame.transform.scale(
            pygame.image.load("images/pets/skeleton/run/tile001.png"), (int(skeletion_size * fix), int(skeletion_size * fix))))
        skeleton_run_sprites.append(pygame.transform.scale(
            pygame.image.load("images/pets/skeleton/run/tile002.png"), (int(skeletion_size * fix), int(skeletion_size * fix))))
        skeleton_run_sprites.append(pygame.transform.scale(
            pygame.image.load("images/pets/skeleton/run/tile003.png"), (int(skeletion_size * fix), int(skeletion_size * fix))))

    gold_spawn_egg = pygame.transform.scale(
        pygame.image.load("images/spawnEggs/Yellow.png"), (int(40 * fix), int(40 * fix)))

    toolBar_item_scale = (int(58 * fix), int(58 * fix))
    toolBar_tier_1_wand = pygame.transform.scale(
        wand_1_Img, toolBar_item_scale)
    toolBar_tier_2_wand = pygame.transform.scale(
        wand_2_Img, toolBar_item_scale)

    petCake = pygame.transform.scale(pygame.image.load(
        "images/petFood/cake.png"), (int(32 * fix), int(32 * fix)))

    pet_cake_item = pygame.transform.scale(
        petCake, (int(35 * fix), int(35 * fix)))
    health_potion_item = pygame.transform.scale(
        health_potion_org, (int(35 * fix), int(35 * fix)))
    mana_potion_item = pygame.transform.scale(
        mana_potionImg_org, (int(35 * fix), int(35 * fix)))
    # 2.5x
    inventory_bg = pygame.transform.scale(pygame.image.load(
        "images/inventory.png"), (int(480 * fix), int(480 * fix)))

    tier_1_wand_item = pygame.transform.scale(
        toolBar_tier_1_wand, (int(35 * fix), int(35 * fix)))
    tier_2_wand_item = pygame.transform.scale(
        toolBar_tier_2_wand, (int(35 * fix), int(35 * fix)))
    skeleton_spawn_egg_item = pygame.transform.scale(
        gold_spawn_egg, (int(35 * fix), int(35 * fix)))
    speedup_boost_item = pygame.transform.scale(
        speedupBoostImg, (int(35 * fix), int(35 * fix)))


pygame.init()


class audio:

    pickPotionSound = pygame.mixer.Sound("audio/pickPotion.mp3")
    slimeWalk = pygame.mixer.Sound("audio/slimeWalk.ogg")
    slimeDeath = pygame.mixer.Sound("audio/slimeDeath.wav")
    shootFireball = pygame.mixer.Sound("audio/shootFireball.wav")
    clickButtonSound = pygame.mixer.Sound("audio/clickButtonSound.wav")
    shootElectricball = pygame.mixer.Sound("audio/shootElectricball.wav")
    usePotionSound = pygame.mixer.Sound("audio/usePotion.wav")
    pickItemSound = pygame.mixer.Sound("audio/pickItem.wav")
    openChestSound = pygame.mixer.Sound("audio/openChest.wav")
    pickCoinSound = pygame.mixer.Sound("audio/pickCoin.wav")
    portalIdleSound = pygame.mixer.Sound("audio/portalIdle.wav")
    teleportSoundd = pygame.mixer.Sound("audio/teleport.wav")
    abortSound = pygame.mixer.Sound("audio/abort.flac")
    tutorSpeak = pygame.mixer.Sound("audio/tutorSpeak.wav")
    dying = pygame.mixer.Sound("audio/dying.wav")
    bling = pygame.mixer.Sound("audio/bling.wav")
    eggCrack = pygame.mixer.Sound("audio/eggCrack.wav")
    ah = pygame.mixer.Sound("audio/ah.wav")
