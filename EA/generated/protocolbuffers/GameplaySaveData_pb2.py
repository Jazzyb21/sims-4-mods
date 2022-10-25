from google.protobuf import descriptor
class ZoneBedInfoData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ZONEBEDINFODATA

class ZoneCurfewData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ZONECURFEWDATA

class LotLevelData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _LOTLEVELDATA

class GameplayZoneData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _GAMEPLAYZONEDATA

class LotUnpaidBillData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _LOTUNPAIDBILLDATA

class HouseholdMilestoneDataTracker(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _HOUSEHOLDMILESTONEDATATRACKER

class Holiday(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _HOLIDAY

class HolidayTracker(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _HOLIDAYTRACKER

class SimPreference(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SIMPREFERENCE

class ZonePreferenceData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ZONEPREFERENCEDATA

class ObjectPreferenceTracker(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _OBJECTPREFERENCETRACKER

class Delivery(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _DELIVERY

class GameplayScenarioTrackerData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _GAMEPLAYSCENARIOTRACKERDATA

class GameplayScenarioData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):

    class ScenarioGoalData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _GAMEPLAYSCENARIODATA_SCENARIOGOALDATA

    class IndexGoalMandatoryTriple(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _GAMEPLAYSCENARIODATA_INDEXGOALMANDATORYTRIPLE

    class SimFilterInfoPair(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _GAMEPLAYSCENARIODATA_SIMFILTERINFOPAIR

    class PhaseOutputInfo(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _GAMEPLAYSCENARIODATA_PHASEOUTPUTINFO

    class CompletedGoalInfo(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _GAMEPLAYSCENARIODATA_COMPLETEDGOALINFO

    class TerminatedPhaseInfo(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _GAMEPLAYSCENARIODATA_TERMINATEDPHASEINFO

    DESCRIPTOR = _GAMEPLAYSCENARIODATA

class GameplayHouseholdData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _GAMEPLAYHOUSEHOLDDATA

class SituationEarnedMedals(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SITUATIONEARNEDMEDALS

class SituationNewEntry(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SITUATIONNEWENTRY

class CollectionData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _COLLECTIONDATA

class RetailData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):

    class RetailDataPayroll(message.Message, metaclass=reflection.GeneratedProtocolMessageType):

        class RetailDataPayrollEntry(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
            DESCRIPTOR = _RETAILDATA_RETAILDATAPAYROLL_RETAILDATAPAYROLLENTRY

        DESCRIPTOR = _RETAILDATA_RETAILDATAPAYROLL

    class RetailFundsCategoryEntry(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _RETAILDATA_RETAILFUNDSCATEGORYENTRY

    DESCRIPTOR = _RETAILDATA

class BucksData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):

    class UnlockedPerk(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _BUCKSDATA_UNLOCKEDPERK

    DESCRIPTOR = _BUCKSDATA

class PersistableClubService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLECLUBSERVICE

class Club(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _CLUB

class PersistableSocialMediaService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLESOCIALMEDIASERVICE

class SocialMediaPostEntry(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALMEDIAPOSTENTRY

class SocialMediaMessageEntry(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALMEDIAMESSAGEENTRY

class SocialMediaDirectMessage(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALMEDIADIRECTMESSAGE

class SocialMediaPost(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALMEDIAPOST

class SocialMediaReaction(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SOCIALMEDIAREACTION

class ServiceNpcRecord(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SERVICENPCRECORD

class AdditionalBillCost(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ADDITIONALBILLCOST

class CurrentBillStatisticDelta(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _CURRENTBILLSTATISTICDELTA

class CurrentBillDetail(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _CURRENTBILLDETAIL

class BillUtilitySettings(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _BILLUTILITYSETTINGS

class PersistableStoryProgressionParticipant(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLESTORYPROGRESSIONPARTICIPANT

class PersistableDramaNode(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEDRAMANODE

class PersistableCallToActionService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLECALLTOACTIONSERVICE

class PersistableLandlordService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLELANDLORDSERVICE

class PersistableTrendService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLETRENDSERVICE

class FashionMarketplaceSoldOutfits(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _FASHIONMARKETPLACESOLDOUTFITS

class PersistableFashionTrendService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEFASHIONTRENDSERVICE

class CooldownDramaNode(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _COOLDOWNDRAMANODE

class DramaNodeCooldownGroup(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _DRAMANODECOOLDOWNGROUP

class PersistableDramaScheduleService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEDRAMASCHEDULESERVICE

class PersistableRelationshipBitLock(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLERELATIONSHIPBITLOCK

class PersistableUnidirectionalRelationshipData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEUNIDIRECTIONALRELATIONSHIPDATA

class PersistableBidirectionalRelationshipData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEBIDIRECTIONALRELATIONSHIPDATA

class PersistableServiceRelationship(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLESERVICERELATIONSHIP

class PersistableRelationshipService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLERELATIONSHIPSERVICE

class PersistableGlobalPolicy(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEGLOBALPOLICY

class PersistableGlobalPolicyBillReduction(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEGLOBALPOLICYBILLREDUCTION

class PersistableGlobalUtilityEffect(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEGLOBALUTILITYEFFECT

class PersistableGlobalPolicyService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEGLOBALPOLICYSERVICE

class AdoptableSimData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ADOPTABLESIMDATA

class PersistableAdoptionService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEADOPTIONSERVICE

class HiddenSimData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _HIDDENSIMDATA

class PersistableHiddenSimService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEHIDDENSIMSERVICE

class PersistableSeasonService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLESEASONSERVICE

class DecorationState(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _DECORATIONSTATE

class LotDecorationSetting(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _LOTDECORATIONSETTING

class DecoratedLocation(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _DECORATEDLOCATION

class HolidayDecorationSetting(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _HOLIDAYDECORATIONSETTING

class WorldDecorationSetting(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _WORLDDECORATIONSETTING

class PersistableLotDecorationService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLELOTDECORATIONSERVICE

class HolidayTimeData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _HOLIDAYTIMEDATA

class HolidayCalendar(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _HOLIDAYCALENDAR

class PersistableHolidayService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEHOLIDAYSERVICE

class StyleOutfitInfo(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _STYLEOUTFITINFO

class PersistableStyleService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLESTYLESERVICE

class RabbitHoleData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _RABBITHOLEDATA

class PersistableRabbitHoleService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLERABBITHOLESERVICE

class NarrativeProgressionData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _NARRATIVEPROGRESSIONDATA

class NarrativeData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _NARRATIVEDATA

class NarrativeLayerData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _NARRATIVELAYERDATA

class PersistableNarrativeService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLENARRATIVESERVICE

class PersistableOrganizationService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEORGANIZATIONSERVICE

class ScheduleEventCallbackData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SCHEDULEEVENTCALLBACKDATA

class OrganizationEventData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ORGANIZATIONEVENTDATA

class OrganizationData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ORGANIZATIONDATA

class OrganizationMemberData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ORGANIZATIONMEMBERDATA

class PersistableObjectLocator(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEOBJECTLOCATOR

class ClonedObjectsLocator(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _CLONEDOBJECTSLOCATOR

class PersistableObjectLostAndFound(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEOBJECTLOSTANDFOUND

class PersistableCullingServiceInteractingSim(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLECULLINGSERVICEINTERACTINGSIM

class PersistableCullingService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLECULLINGSERVICE

class PersistableUniversityStoryProgressionAction(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEUNIVERSITYSTORYPROGRESSIONACTION

class PersistableStoryProgressionService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLESTORYPROGRESSIONSERVICE

class PersistableCivicPolicyCustomData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLECIVICPOLICYCUSTOMDATA

class PersistableDefaultConditionalLayerData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEDEFAULTCONDITIONALLAYERDATA

class PersistableCivicPolicyProviderData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLECIVICPOLICYPROVIDERDATA

class PersistableStreetEcoFootprintData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLESTREETECOFOOTPRINTDATA

class PersistableStreetData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLESTREETDATA

class PersistableStreetService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLESTREETSERVICE

class PersistableCivicPolicyStreetPolicyData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLECIVICPOLICYSTREETPOLICYDATA

class PersistableCivicPolicyStreetConditionalLayerEffectData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLECIVICPOLICYSTREETCONDITIONALLAYEREFFECTDATA

class PersistableRegionData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEREGIONDATA

class PersistableRegionService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEREGIONSERVICE

class PersistableLifestyleService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLELIFESTYLESERVICE

class PersistableABTestService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):

    class ABTestData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _PERSISTABLEABTESTSERVICE_ABTESTDATA

    DESCRIPTOR = _PERSISTABLEABTESTSERVICE

class PersistableLiveEventService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):

    class LiveEventData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _PERSISTABLELIVEEVENTSERVICE_LIVEEVENTDATA

    DESCRIPTOR = _PERSISTABLELIVEEVENTSERVICE

class PersistableAssignedAnimals(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEASSIGNEDANIMALS

class PersistableAnimalService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEANIMALSERVICE

class PresistablePurchasePickerGroupItem(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PRESISTABLEPURCHASEPICKERGROUPITEM

class PersistablePurchasePickerGroupData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEPURCHASEPICKERGROUPDATA

class PersistablePurchasePickerService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEPURCHASEPICKERSERVICE

class PersistableLunarCycleService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLELUNARCYCLESERVICE

class PersistableClanService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLECLANSERVICE

class ClanLeaderData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _CLANLEADERDATA

class ClanMembersData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _CLANMEMBERSDATA

class PersistableGraduationService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEGRADUATIONSERVICE

class PersistableVenueGameService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEVENUEGAMESERVICE

class PersistablePromService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLEPROMSERVICE

class PersistableCareerService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLECAREERSERVICE

class GameplaySaveSlotData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _GAMEPLAYSAVESLOTDATA

class PersistableRelgraphService(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PERSISTABLERELGRAPHSERVICE

class GameplayCameraData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _GAMEPLAYCAMERADATA

class GameplayNeighborhoodData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _GAMEPLAYNEIGHBORHOODDATA

class GameplayAccountData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _GAMEPLAYACCOUNTDATA

class AccountEventDataTracker(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ACCOUNTEVENTDATATRACKER

class GameplayOptions(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _GAMEPLAYOPTIONS

class RestaurantZoneDirectorData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):

    class TableGroup(message.Message, metaclass=reflection.GeneratedProtocolMessageType):

        class SimSeat(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
            DESCRIPTOR = _RESTAURANTZONEDIRECTORDATA_TABLEGROUP_SIMSEAT

        DESCRIPTOR = _RESTAURANTZONEDIRECTORDATA_TABLEGROUP

    class SavedDailySpecial(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _RESTAURANTZONEDIRECTORDATA_SAVEDDAILYSPECIAL

    class GroupOrder(message.Message, metaclass=reflection.GeneratedProtocolMessageType):

        class FoodAndDrink(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
            DESCRIPTOR = _RESTAURANTZONEDIRECTORDATA_GROUPORDER_FOODANDDRINK

        DESCRIPTOR = _RESTAURANTZONEDIRECTORDATA_GROUPORDER

    DESCRIPTOR = _RESTAURANTZONEDIRECTORDATA

class ZoneDirectorCleanupActionData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ZONEDIRECTORCLEANUPACTIONDATA

class ZoneDirectorSituationData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ZONEDIRECTORSITUATIONDATA

class ZoneDirectorData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ZONEDIRECTORDATA

class VenueData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _VENUEDATA

class OpenStreetDirectorData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _OPENSTREETDIRECTORDATA

class ConditionalLayerInfo(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _CONDITIONALLAYERINFO

class ConditionalLayerServiceData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _CONDITIONALLAYERSERVICEDATA

class AmbientSourceData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _AMBIENTSOURCEDATA

class AmbientServiceData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _AMBIENTSERVICEDATA

class InteractionSaveData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _INTERACTIONSAVEDATA

class TransitioningInteraction(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _TRANSITIONINGINTERACTION

class SuperInteractionSaveState(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SUPERINTERACTIONSAVESTATE

class WorldLocation(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _WORLDLOCATION

class ZoneTimeStamp(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ZONETIMESTAMP

class WhimsetTrackerData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):

    class WhimData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _WHIMSETTRACKERDATA_WHIMDATA

    DESCRIPTOR = _WHIMSETTRACKERDATA

class AwayActionData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _AWAYACTIONDATA

class AwayActionTrackerData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _AWAYACTIONTRACKERDATA

class SimFavoriteData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SIMFAVORITEDATA

class GameplaySimData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _GAMEPLAYSIMDATA

class PremadeLotStatus(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PREMADELOTSTATUS

class EnsembleServiceData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ENSEMBLESERVICEDATA

class EnsembleData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ENSEMBLEDATA

class MissingPetTrackerData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _MISSINGPETTRACKERDATA

class MotiveTestResults(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _MOTIVETESTRESULTS

class LaundryData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _LAUNDRYDATA

class LaundryConditions(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _LAUNDRYCONDITIONS

class HiddenSimServiceData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _HIDDENSIMSERVICEDATA
